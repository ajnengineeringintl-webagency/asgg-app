from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint, url_for, flash, jsonify,render_template, session,redirect, request, current_app
from app.database import asgg_app_database_models_authentication, asgg_app_database_models_dashboard_data_recordings_dataRecordings

import os
import datetime
from werkzeug.utils import secure_filename
import math
asgg_app_dashboard_routes = Blueprint("asgg_app_dashboard_routes", __name__, template_folder="templates", static_folder="static")
@asgg_app_dashboard_routes.route("/", methods=["GET","POST"])
def asgg_dashboard():
    if 'authenticated_userid' not in session:
         print("not signed in found")
         
         return redirect(url_for("asgg_app_authentication_routes.asgg_signin"))
    
    userid = session.get("authenticated_userid")
    
    authenticated_user_by_id = asgg_app_database_models_authentication.query.get(userid)
   

    if not authenticated_user_by_id:
         print("no user found")
         return redirect(url_for("asgg_app_authentication_routes.asgg_signup"))
    signeduser = authenticated_user_by_id.dt()
    recordings = asgg_app_database_models_dashboard_data_recordings_dataRecordings.query.all()
    dashboard_recordings_data = []
    users =[]
    authenticated_user = asgg_app_database_models_authentication.query.all()
    try:
        db.session.commit()

        for i in authenticated_user:
            print("user loading")
            users.append(i.dt())

        for record in recordings:
            print("record loading")
            dashboard_recordings_data.append(record.dt()) 
            
        flash("succesfull signin")
        print("succesfull signin")

        print("succes")#jsonify({"user":authenticated_user})#redirect(url_for("dashboard.asgg_dashboard"))
    except Exception as e:
            flash("error")
            print(Exception)
            
    
    return render_template('dashboard_v1_0_1_0.html',data=users,signed_user=signeduser,recordedpodcasts=dashboard_recordings_data)
"""rendering dashboard online!200 Hello Word"""
@asgg_app_dashboard_routes.route("/dashboard-v1", methods=["POST","GET"])
def asgg_new_dashboard_v1():
    #if 'authenticated_userid' not in session:
    #    print("not signed in found")
        
    #    return redirect(url_for("asgg_app_authentication_routes.asgg_signin"))
    
    userid = 1
    
    authenticated_user_by_id = asgg_app_database_models_authentication.query.get(userid)
    

    #if not authenticated_user_by_id:
    #    print("no user found") in
    #    return redirect(url_for("asgg_app_authentication_routes.asgg_signup"))
    signeduser = authenticated_user_by_id.dt()
    recordings = asgg_app_database_models_dashboard_data_recordings_dataRecordings.query.all()
    dashboard_recordings_data = []
    users =[]
    authenticated_user = asgg_app_database_models_authentication.query.all()
    try:
        db.session.commit()

        for i in authenticated_user:
            print("user loading")
            users.append(i.dt())

        for record in recordings:
            print("record loading")
            dashboard_recordings_data.append(record.dt()) 
            
        flash("succesfull signin")
        print("succesfull signin")

        print("succes")#jsonify({"user":authenticated_user})#redirect(url_for("dashboard.asgg_dashboard"))
    except Exception as e:
            flash("error")
            print(Exception)
    return render_template('dashboard.html',data=users,signed_user=signeduser,recordedpodcasts=dashboard_recordings_data)


@asgg_app_dashboard_routes.route("/recordings", methods=["POST"])
def asgg_recordings():
      if 'authenticated_userid' not in session:
               print("not signed in found")
               
               return jsonify({'error':'user notsigned in'})
      if request.method == "POST":
        recording_title = request.form['title']
        recording_information = request.form['information']
        recording_upload_status = request.form['status']
        recording_cover_img = request.files['img']
        podcast_websites = request.form.getlist('podcast-websites')
        upload_links_youtube = str(request.form['youtube-link'])
        upload_links_rss = str(request.form['rss-link'])
        upload_links_facebook = str(request.form['facebook-link'])
        upload_links_mixlr = request.form['mixlr-link']
        upload_links_buzzsprout = request.form['buzzsprout-link']
        filename = secure_filename(recording_cover_img.filename)
        new_filename = f"_{filename}"
        print(new_filename)
        new_path = f"http://127.0.0.1:4700/static/recordings-images/{new_filename}"

        save_path = os.path.join(current_app.config["UPLOAD_FOLDER" ], new_filename)
        print(save_path)
        recording_cover_img.save(save_path)
        print(recording_title)
        #print(recording_recorder)
        print(podcast_websites)
        #,recorded=recording_date view
        new_recording_podcast = asgg_app_database_models_dashboard_data_recordings_dataRecordings(title=recording_title,information=recording_information,recording_uploaded_to_website=podcast_websites,upload_status=recording_upload_status,recording_cover_img=new_path,upload_link_youtube=upload_links_youtube,upload_link_rss=upload_links_rss,upload_link_buzzsprout=upload_links_buzzsprout,upload_link_facebook=upload_links_facebook,upload_link_mixlr=upload_links_mixlr)
        try:
            db.session.add(new_recording_podcast)
            db.session.commit()
            print("new")
            return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))#jsonify({"new":authenticated_user.dt() })
        except Exception as e:
            print("succesful: but error", e)
            return jsonify({'error':str(e)})
      return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))#jsonify({"new":authenticated_user.dt() })
@asgg_app_dashboard_routes.route("/recordings", methods=["GET"])
def asgg_recordings_edit_add():
     if 'authenticated_userid' not in session:
            print("not signed in found")
            
            return redirect(url_for("asgg_app_authentication_routes.asgg_signin"))
     return render_template("recordings.html")
@asgg_app_dashboard_routes.route("/recordings/edit/<rcid>", methods=["GET","PUT"])
def asgg_recordings_edit(rcid):
        recordingid = rcid
  
        recordings = asgg_app_database_models_dashboard_data_recordings_dataRecordings.query.get(recordingid)
        #db.session.commit()
        if not recordings:
            return "recording not found"
        if request.method == "PUT":
            dataforrecord = recordings.dt()
            data = request.get_json()
            print(f"data : {data}")
            recording_title = data['title']
            recording_information =  data['information']
            recording_upload_status =  data['status']
            dataforrecord.title = recording_title
            dataforrecord.information = recording_information
            dataforrecord.upload_status = recording_upload_status
            try:
                db.session.commit()
                print(f"new data save: {data}")
                return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))#jsonify({"new":authenticated_user.dt() })
            except Exception as e:
              return f"error :{e}"
        return render_template("recordings-edit.html",data=recordings)
@asgg_app_dashboard_routes.route("/profile/put/<userid>", methods=["POST","PUT","GET"])
def asgg_edit_user_info(userid):
     try:
        user = asgg_app_database_models_authentication.query.get(userid)
        if not user:
            return "user found not"
       
        user_name = request.form['name']
        user_email = request.form['email']
        user_passw = request.form['passw']

        user.name = user_name
        user.email = user_email
        user.passw = user_passw

        db.session.commit()
        return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))#jsonify({"new":authenticated_user.dt() })
        
     except:
         return '"error":"something went wrong trying to change info"'
@asgg_app_dashboard_routes.route("/profile/<userid>", methods=["PUT","GET"])
def asgg__user_info(userid):
     user = asgg_app_database_models_authentication.query.get(userid)
     if not user:
        return "user found not"
     data=user.dt()
     return render_template("edit-user-info.html",template_info=data)
@asgg_app_dashboard_routes.route("/recordings/veiw/<rcid>", methods=["GET"])
def asgg_recordings_edit_ad(rcid):
     recordingid = rcid
     recordings = asgg_app_database_models_dashboard_data_recordings_dataRecordings.query.get(recordingid)
     #db.session.commit()
     if not recordings:
        return "recording not found"
     else:
        dataforrecord = recordings.dt()
        print("hello, update to save record")
        return render_template("recordings-edit.html",data=dataforrecord)
@asgg_app_dashboard_routes.route("/recordings/delete/<rcid>", methods=["GET"])
def asgg_recordings_edit_delete(rcid):
     recordingid = rcid
     recordings = asgg_app_database_models_dashboard_data_recordings_dataRecordings.query.get(recordingid)
     if not recordings:
             return "recording not found"
     db.session.delete(recordings)
     db.session.commit()
     print(f"error not found:user recording {recordings.dt()} has been deleted")
     # return(f"error not found:user recording {recordings.dt()} has been deleted <a href='/' class='btn'>Das</a>")
     return redirect(url_for("asgg_app_dashboard_routes.asgg_dashboard"))#jsonify({"new":authenticated_user.dt() })



     
           
            