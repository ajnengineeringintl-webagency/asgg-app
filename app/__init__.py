from flask import Flask, Blueprint, url_for, jsonify,render_template, session, redirect, request
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from datetime import timedelta

load_dotenv()
db = SQLAlchemy()
def asgg_app_server(): 
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SECRET_KEY"] =os.environ.get("ASGGAPPSECRETKEY")

    app.config["AVATER_UPLOAD_FOLDER" ] = os.path.join("app/static", "images")
    app.config["UPLOAD_FOLDER"] = os.path.join("app/static", "recordings-images")

    app.config["MAX_UPLOAD_LENGTH"] = 5 * 1024 * 1024

    app.config["SESSION_COOKIE_HTTPONLY"] =True
    app.config["SESSION_COOKIE_SECURE"] =True
    app.config["SESSION_COOKIE_SAMESITE"] = 'Lax'
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)

    db.init_app(app)

    os.makedirs(app.config["UPLOAD_FOLDER"] , exist_ok=True)    

    from .authentication import asgg_app_authentication_routes
    from .dashboard import asgg_app_dashboard_routes
    from .database import asgg_app_database_models_authentication, asgg_app_database_models_dashboard_data_recordings_dataRecordings
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(asgg_app_authentication_routes, url_prefix="/authentication")
    app.register_blueprint(asgg_app_dashboard_routes, url_prefix="/")

    '''PRAISE THE LORD'''
    return app
