from app import asgg_app_server
import os

'''PRIASE THE LORD'''
app = asgg_app_server()

if __name__ == "__main__":
    app.run(debug=True,port=os.environ.get("ASGG_APP_PORTNUMBER"))