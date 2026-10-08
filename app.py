import os
from flask import Flask
from models.models import db, user_info

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

# Secret key configuration for sessions
app.secret_key = os.environ.get("SECRET_KEY", "qm_default_dev_secret_key_2026")

# Database configuration (PostgreSQL for cloud, SQLite for local)
db_url = os.environ.get("DATABASE_URL")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Debug mode
app.debug = os.environ.get("FLASK_DEBUG", "1").lower() in ("1", "true")

db.init_app(app)
app.app_context().push()

def create_db_and_admin():
    db.create_all()
    admin_email = os.environ.get("ADMIN_EMAIL", "admin@iitm")
    admin_pwd = os.environ.get("ADMIN_PASSWORD", "admin123")
    if not user_info.query.filter_by(email=admin_email).first():
        admin = user_info(
            name="Admin",
            email=admin_email,
            password=admin_pwd,
            qualification="Admin",
            dob="",
            role=0
        )
        db.session.add(admin)
        db.session.commit()

create_db_and_admin()

from controllers.controllers import *

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)