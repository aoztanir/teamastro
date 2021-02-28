from flask import Flask, render_template, request, session
# from oauth import Oauth
from threading import Thread


app = Flask(__name__)
app.config["SECRET_KEY"] = "test123"

@app.route("/")
def home():
	return render_template("index.html")

# @app.route("/login")
# def login():
# 	code = request.args.get("code")

# 	at = Oauth.get_access_token(code)
# 	session["token"] = at

# 	user = Oauth.get_user_json(at)
# 	user_name, user_id = user.get("username"), user.get("discriminator")

# 	return f"Success, logged in as {user_name}#{user_id}"

def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()