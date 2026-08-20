from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, url_for, jsonify,render_template, session, redirect, request, flash, current_app
from app.database import asgg_app_database_models_authentication

import os
from werkzeug.utils import secure_filename
asgg_app_authentication_routes = Blueprint("asgg_app_authentication_routes", __name__, template_folder="templates", static_folder="static")
@asgg_app_authentication_routes.route("/signin", methods=["GET","POST"])
def asgg_signin():
    if request.method == "POST":
        email = request.form['email']
        passw = request.form['passw']

        
        authenticated_user = asgg_app_database_models_authentication.query.filter((asgg_app_database_models_authentication.email==email)).first()
        try:
            db.session.commit()
            
                
            flash("succesfull signin")
            print("succesfull signin")
            if authenticated_user is None:
                return jsonify({"error":"no authenticated_user"})

            user = authenticated_user.dt()
            print(user)
            session["authenticated_userid"] = user["userid"]
            return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))#jsonify({"user":authenticated_user.dt()})
        except Exception as e:
                flash("error")
                print(Exception)
                return jsonify({"error":str(authenticated_user.dt())})
        
    return render_template('authentication.html')
#''' rendering signin online!200 Hello Word'''
@asgg_app_authentication_routes.route("/create-account", methods=["GET","POST"])
def asgg_signup():
    if request.method == "POST":
        user_name = request.form['name']
        user_email = request.form['email']
        user_passw = request.form['passw']
        user_avater = request.files['user_avater']
        social_links_youtube = request.form['youtube-link']
        social_links_rss = request.form['rss-link']
        social_links_facebook = request.form['facebook-link']
        social_links_mixlr = request.form['mixlr-link']
        social_links_buzzsprout = request.form['buzzsprout-link']
        if not user_avater:
            
            authenticated_user = asgg_app_database_models_authentication(name=user_name,email=user_email,passw=user_passw,social_links_youtube=social_links_youtube,social_links_rss=social_links_rss,social_links_facebook=social_links_facebook,social_links_mixlr=social_links_mixlr,social_links_buzzsprout=social_links_buzzsprout)
        else:
            print(user_name)
            print(user_email)
            print(user_passw)
            
            filename = secure_filename(user_avater.filename)
            new_filename = f"_{filename}"
            print(new_filename)
            new_path = f"http://127.0.0.1:4700/static/images/{new_filename}"

            save_path = os.path.join(current_app.config["AVATER_UPLOAD_FOLDER" ], new_filename)
            print(save_path)
            user_avater.save(save_path)
            print("uploading image avater...")
            authenticated_user = asgg_app_database_models_authentication(name=user_name,email=user_email,passw=user_passw,user_avater=new_path,social_links_youtube=social_links_youtube,social_links_rss=social_links_rss,social_links_facebook=social_links_facebook,social_links_mixlr=social_links_mixlr,social_links_buzzsprout=social_links_buzzsprout)
        try:
            db.session.add(authenticated_user)
            db.session.commit()
            print("new")
            return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))#jsonify({"new":authenticated_user.dt() })
        except Exception as e:
            print("succesful: but error", e)
            return jsonify({'error':str(e)})


    
    return render_template('create-account.html')
    #redirect(url_for("app.dashboard.asgg_dashboard"))
    #"""rendering signup online!200 Hello Word n"""

@asgg_app_authentication_routes.route("/signout", methods=["GET","POST"])
def asgg_signout():    
     session.pop("authenticated_userid",None)
     return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))
