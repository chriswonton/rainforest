from flask import Blueprint, request, session, jsonify, render_template
from services.product_service import ProductService

product_bp = Blueprint('product', __name__)
product_service = ProductService()

@product_bp.route('/products')
def products():
    user = session.get('user')
    products = product_service.get_all_products()
    return render_template('product/products.html', user=user, products=products)

@product_bp.route('/products/<int:product_id>')
def product_page(product_id):
    user = session.get('user')
    product = product_service.get_product_by_id(product_id)
    return render_template('product/product.html', user=user, product=product)

@product_bp.route('/products/<int:product_id>', methods=['POST'])
def add_order(product_id):
    user = session.get('user')
    if not user:
        return jsonify({"error": "User not logged in"}), 401
    
    data = request.get_json()
    quantity = data['quantity']
    
    message, error = product_service.add_order(user, product_id, quantity)
    if error:
        return jsonify({"error": error}), 400
    
    return jsonify({"message": message}), 201

@product_bp.route('/shopping_cart')
def shopping_cart():
    user = session.get('user')
    if not user:
        return jsonify({"error": "User not logged in"}), 401
    
    order_items, total_price, error = product_service.get_shopping_cart(user)
    if error:
        return jsonify({"error": error}), 400
    
    return render_template('product/shopping_cart.html', order_items=order_items, total_price=total_price)

@product_bp.route('/shopping_cart', methods=['POST'])
def buy():
    user = session.get('user')
    if not user:
        return jsonify({"error": "User not logged in"}), 401
    
    message, error = product_service.buy_items(user)
    if error:
        return jsonify({"error": error}), 400
    
    return jsonify({"message": message}), 201
