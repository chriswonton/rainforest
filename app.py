from flask import *
import hashlib
import db_operations as db

app = Flask(__name__)
user = None
admin = 0

@app.route('/')
def main():
    return render_template('home.html', user = user, admin = admin)

@app.route('/', methods=['POST'])
def logout():
    global user
    global admin
    user = None
    admin = 0
    return jsonify({"message": "Logged out successfully"}), 201

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/login', methods=['POST'])
def validate_login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    account = db.select_account_username(username)

    if (account == None):
        account = db.select_account_email(username)
        if (account == None):
            return jsonify({"error": "Account not found"}), 404

    if (encrypt_password(password) != account[2]):
        return jsonify({"error": "Invalid password"}), 401
    
    global user
    user = account[1]
    if (account[5] == 1):
        global admin
        admin = 1
    return jsonify({"message": "Logged in successfully"}), 201

@app.route('/signup')
def signup():
    return render_template('auth/signup.html')

@app.route('/signup', methods=['POST'])
def validate_signup():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    password2 = data['password2']

    accounts = db.select_all_accounts()

    for account in accounts:
        if (username == account[1]):
            return jsonify({"error": "Username already exists"}), 401
        if (email == account[3]):
            return jsonify({"error": "Email already taken"}), 401

    if (password != password2):
        return jsonify({"error": "Password 1 does not match Password 2"}), 401
    
    password = encrypt_password(password)

    db.insert_account(username, password, email)
    global user
    user = username
    return jsonify({"message": "Signed up successfully"}), 201

@app.route('/admin')
def admin():
    return render_template('/admin.html')

@app.route('/admin', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    manufacturer = data['manufacturer']
    description = data['description']
    image = data['image']
    category = data['category']
    price = data['price']
    stock = data['stock']

    db.insert_product(name, manufacturer, description, image, category, price, stock)
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products')
def products():
    products = db.select_all_products()
    return render_template('/products.html', products = products)

@app.route('/products/<int:product_id>')
def product_page(product_id):
    product = db.select_product_id(product_id)
    return render_template('/product.html', product = product)

@app.route('/products/<int:product_id>', methods=['POST'])
def add_order(product_id):
    account = db.select_account_username(user)
    account_id = account[0]
    order_id = db.select_order_cart(account_id)
    if order_id == None:
        order_id = db.insert_order(account_id)
    
    data = request.get_json()
    quantity = data['quantity']

    db.insert_order_item(order_id, product_id, quantity)
    return jsonify({"message": "Product added to shopping cart"}), 201

@app.route('/shopping_cart')
def shopping_cart():
    account = db.select_account_username(user)
    account_id = account[0]
    order_id = db.select_order_cart(account_id)
    if order_id == None:
        order_id = db.insert_order(account_id)
    
    order_items = db.select_order_item_id(order_id)
    total_price = 0
    for product in order_items:
        total_price += (product[5] * product[2])

    return render_template('/shopping_cart.html', order_items = order_items, total_price = total_price)

@app.route('/shopping_cart', methods=['POST'])
def buy():
    account = db.select_account_username(user)
    account_id = account[0]
    order_id = db.select_order_cart(account_id)
    if order_id == None:
        order_id = db.insert_order(account_id)
    
    db.update_product_stock(order_id)
    db.update_order_date(order_id)
    
    return jsonify({"message": "Bought items"}), 201

def encrypt_password(password):
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(password_bytes)
    hashed_password = hash_object.hexdigest()
    
    return hashed_password

if __name__ == '__main__':
    app.run(debug=True)
