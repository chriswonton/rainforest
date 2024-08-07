from flask import Blueprint, request, session, jsonify, render_template
from services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()

@user_bp.route('/')
def main():
    user = session.get('user')
    admin = session.get('admin', 0)
    return render_template('home.html', user=user, admin=admin)

@user_bp.route('/', methods=['POST'])
def logout():
    session.pop('user', None)
    session.pop('admin', None)
    return jsonify({"message": "Logged out successfully"}), 201

@user_bp.route('/login')
def login():
    return render_template('auth/login.html')

@user_bp.route('/login', methods=['POST'])
def validate_login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    account, error = user_service.validate_login(username, password)
    if error:
        return jsonify({"error": error}), 401
    
    session['user'] = account[1]
    session['admin'] = 1 if account[5] == 1 else 0
    return jsonify({"message": "Logged in successfully"}), 201

@user_bp.route('/signup')
def signup():
    return render_template('auth/signup.html')

@user_bp.route('/signup', methods=['POST'])
def validate_signup():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    password2 = data['password2']

    error = user_service.validate_signup(username, email, password, password2)
    if error:
        return jsonify({"error": error}), 401

    session['user'] = username
    return jsonify({"message": "Signed up successfully"}), 201
