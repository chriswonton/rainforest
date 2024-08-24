from flask import *
from routes.admin_route import admin_bp
from routes.user_route import user_bp
from routes.product_route import product_bp
import os
from dotenv import load_dotenv
from schedulers.user_tasks import start_scheduler

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

if __name__ == '__main__':
    start_scheduler()
    app.run(debug=True)
