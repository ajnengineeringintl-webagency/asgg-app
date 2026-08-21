from flask import Flask, Blueprint, url_for, jsonify,render_template, session, redirect, request
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from datetime import timedelta

load_dotenv()
db = SQLAlchemy()
def asgg_app_server(): 
    application = Flask(__name__)
    
    database = os.getenv("DATABASE")
    if database and database.startswith('postgres://'):
        database =  database.replace('postgres://', 'postgresql://',1)
    application.config["SQLALCHEMY_DATABASE_URI"] = database
    application.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_size":1,
        "max_overflow":0,
        "pool_recycle":120,
        "pool_pre_ping":True
    }
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    application.config["SECRET_KEY"] =os.environ.get("ASGGAPPSECRETKEY")

    application.config["AVATER_UPLOAD_FOLDER" ] = os.path.join("app/static", "images")
    application.config["UPLOAD_FOLDER"] = os.path.join("app/static", "recordings-images")

    application.config["MAX_UPLOAD_LENGTH"] = 5 * 1024 * 1024

    application.config["SESSION_COOKIE_HTTPONLY"] =True
    application.config["SESSION_COOKIE_SECURE"] =True
    application.config["SESSION_COOKIE_SAMESITE"] = 'Lax'
    application.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)

    db.init_app(application)

    os.makedirs(application.config["UPLOAD_FOLDER"] , exist_ok=True)    

    from .authentication import asgg_app_authentication_routes
    from .dashboard import asgg_app_dashboard_routes
    from .database import asgg_app_database_models_authentication, asgg_app_database_models_dashboard_data_recordings_dataRecordings
    with application.app_context():
        db.create_all()
    
    application.register_blueprint(asgg_app_authentication_routes, url_prefix="/authentication")
    application.register_blueprint(asgg_app_dashboard_routes, url_prefix="/")

    '''PRAISE THE LORD'''
    return application
