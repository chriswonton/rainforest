# Router uses service ==> invoked from UI
# Service uses repository ==> contain business logic, compute, validation
# Repository accesses DB ==> No business logic, just CRUD operations

from flask import *
from services.admin_service import AdminService

admin_bp = Blueprint('admin', __name__)
admin_service = AdminService()

@admin_bp.route('/admin')
def admin():
    return render_template('admin.html')

@admin_bp.route('/admin', methods=['POST'])
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

@admin_bp.route('/admin/product_management')
def product_managment():
    return render_template('/product_management.html')