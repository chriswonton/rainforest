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

@app.route('/products')
def products():
    return render_template('/products.html')

@app.route('/account', methods=['POST'])
def add_account():
    data = request.json
    db.insert_account(data['username'], data['password'], data['email'])
    return jsonify({"message": "Account created successfully"}), 201

@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    db.insert_product(data['name'], data['description'], data['price'], data['stock'])
    return jsonify({"message": "Product created successfully"}), 201

# @app.route('/order', methods=['POST'])
# def add_order():
#     data = request.json
#     order_id = db.insert_order(data['account_id'], data['total'])
#     return jsonify({"order_id": order_id, "message": "Order created successfully"}), 201

# @app.route('/order_product', methods=['POST'])
# def add_order_product():
#     data = request.json
#     db.insert_order_product(data['order_id'], data['product_id'], data['quantity'])
#     return jsonify({"message": "Order-Product entry created successfully"}), 201

# @app.route('/shipment', methods=['POST'])
# def add_shipment():
#     data = request.json
#     db.insert_shipment(data['order_id'], data['delivery_date'], data['status'])
#     return jsonify({"message": "Shipment created successfully"}), 201


def encrypt_password(password):
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(password_bytes)
    hashed_password = hash_object.hexdigest()
    
    return hashed_password

if __name__ == '__main__':
    app.run(debug=True)
