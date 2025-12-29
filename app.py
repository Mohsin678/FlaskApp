from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "index page"


@app.route("/home")
def welcome():
    return "welcome to home page"

if __name__=="__main__":
    app.run(debug=True)