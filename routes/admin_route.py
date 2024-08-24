# Router uses service ==> invoked from UI
# Service uses repository ==> contain business logic, compute, validation
# Repository accesses DB ==> No business logic, just CRUD operations

from flask import *
from services.admin_service import AdminService

admin_bp = Blueprint('admin', __name__)
admin_service = AdminService()

@admin_bp.route('/admin')
def admin():
    return render_template('admin/admin.html')

@admin_bp.route('/admin/product_management')
def product_management():
    return render_template('admin/product_management.html')

@admin_bp.route('/admin/product_management', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    manufacturer = data['manufacturer']
    description = data['description']
    image = data['image']
    category = data['category']
    price = data['price']
    stock = data['stock']

    admin_service.insert_product(name, manufacturer, description, image, category, price, stock)
    return jsonify({"message": "Product added successfully"}), 201

@admin_bp.route('/admin/user_management')
def user_management():
    users = admin_service.get_all_users()
    response = make_response(render_template('admin/user_management.html', users=users))
    return response

@admin_bp.route('/admin/user_management', methods=['POST'])
def edit_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    is_admin = data['admin']
    is_active = data['active']
    
    admin_service.update_user(username, email, is_admin, is_active)
    
    return jsonify({"message": "User updated successfully"}), 200
