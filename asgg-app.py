from app import asgg_app_server
import os

'''PRIASE THE LORD'''
asgg_app = asgg_app_server()
if __name__ == "__main__":
    asgg_app.run(debug=True,port=os.environ.get("ASGG_APP_PORTNUMBER"))