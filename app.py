from flask import Flask
from models.models import db, user_info
import os

app= None

def quiz_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_master.db'
    app.debug = True
    db.init_app(app)
    app.app_context().push() # to access other modules(outside app.py) that uses app

def create_db_and_admin():
    if not os.path.exists('quiz_master.db'):
        db.create_all()
        if not user_info.query.filter_by(email="admin@iitm").first():
            admin = user_info(name="Admin", email="admin@iitm", password="admin123",qualification="Admin",dob="" ,role=0)
            db.session.add(admin)
            db.session.commit()

quiz_app()
create_db_and_admin()

from controllers.controllers import *

if __name__ == "__main__":
    app.run()