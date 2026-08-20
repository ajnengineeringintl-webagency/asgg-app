from app import db
from flask_sqlalchemy import SQLAlchemy

class asgg_app_database_models_authentication(db.Model):
  __tablename__ = "asgg_app_database_models_authentication"
  userid= db.Column(db.Integer,primary_key=True,unique=True)
  name= db.Column(db.Text,nullable=False)
  email= db.Column(db.Text,nullable=False,unique=True)
  passw= db.Column(db.Text,nullable=False)
  website_link_= db.Column(db.Text,nullable=True)
  social_links_youtube= db.Column(db.Text,nullable=False)
  social_links_rss= db.Column(db.Text,nullable=False)
  social_links_facebook= db.Column(db.Text,nullable=False)
  social_links_mixlr= db.Column(db.Text,nullable=False)
  social_links_buzzsprout= db.Column(db.Text,nullable=False)
  user_avater=db.Column(db.Text(), default="http://127.0.0.1:4700/static/images/user-avater.png", nullable=False)
  joined=db.Column(db.DateTime(timezone=True), default=db.func.now(),nullable=False)
  def dt(self):
    return {"name":self.name,"userid":self.userid,"user_avater":self.user_avater,"email":self.email,"password":self.passw,"date_joined":self.joined,"social_links_youtube":self.social_links_youtube,"social_links_rss":self.social_links_rss,"social_links_facebook":self.social_links_facebook,"social_links_mixlr":self.social_links_mixlr,"social_links_buzzsprout":self.social_links_buzzsprout}

class asgg_app_database_models_dashboard_data_recordings_dataRecordings(db.Model):
  __tablename__ = "asgg_app_database_models_dashboard_data_recordings_dataRecordings"
  recordingid= db.Column(db.Integer,primary_key=True)
  title= db.Column(db.String(),nullable=False)
  recorder=db.Column(db.String(),default="ARISE AND SHINE IN GOD'S GLORY")
  upload_link_youtube= db.Column(db.Text(),unique=True)
  upload_link_rss= db.Column(db.Text(),unique=True)
  upload_link_facebook= db.Column(db.Text(),unique=True)
  upload_link_mixlr= db.Column(db.Text(),unique=True)
  upload_link_buzzsprout= db.Column(db.Text(),unique=True)
  information= db.Column(db.String(),nullable=False)
  upload_status= db.Column(db.String(),nullable=False, default="Online")
  recorded=db.Column(db.DateTime(), default=db.func.now(), nullable=False)
  recording_cover_img=db.Column(db.Text(), default="http://127.0.0.1:4700/static/recordings-images/'Arise_Shine.png", nullable=False)
  recording_uploaded_to_website=db.Column(db.JSON(), default=[])

  def dt(self):
    return {"title":self.title,"recording_cover_img":self.recording_cover_img,"recordingid":self.recordingid,"information":self.information, "recorded":self.recorded,"upload_status":self.upload_status,"recorder":self.recorder,"recording_uploaded_to_website":self.recording_uploaded_to_website,"upload_link_youtube":self.upload_link_youtube,"upload_link_rss":self.upload_link_rss,"upload_link_facebook":self.upload_link_facebook,"upload_link_mixlr":self.upload_link_mixlr,"upload_link_buzzsprout":self.upload_link_buzzsprout}
  #
  #j
  #,#
  #
  #"
  #,"recordings":self.recordings}
  #recordings= db.Relationship("asgg_app_database_models_dashboard_data_recordings_dataRecordings",backref="user",lazy=True)
  #  passw= db.Column(db.Text(),nullable=False)
  #  user= db.Column(db.Integer, db.ForeignKey("asgg_app_database_models_authentication.userid"), nullable=False)
 
  #user":self.user, '''s'''
  