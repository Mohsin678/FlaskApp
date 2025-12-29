from flask import Flask,request,render_template,redirect,url_for


app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to home page"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score>=50:
        res = "passed"
    else:
        res ="failed"

    return render_template("result.html",results =res)


@app.route("/successres/<int:score>")
def successres(score):
    res = " "
    if score>=50:
        res = "passed"
    else:
        res = "failed"
    exp = {"score":score,"res":res}
    return render_template("result1.html",results= exp)

@app.route("/submit",methods=["GET","POST"])
def submit():
    tot_score = 0
    if request.method=="POST":
        science = float(request.form["science"])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for("successres",score = tot_score))

if __name__=="__main__":
    app.run(debug=True)