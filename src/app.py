from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
	return {"success":True, "message":os.environ['message']}


if __name__ == "__main__":
	app.run(debug=True)