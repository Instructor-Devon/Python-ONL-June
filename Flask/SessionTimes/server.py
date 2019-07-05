from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secretsss"

@app.route("/")
def index():
    # general initializion, check for keys in session

    # session["count"] = 0

    if not "count" in session:
        session["count"] = 0

    # we want to keep track of all users submitted
    if not "users" in session:
        session["users"] = []

    return render_template("index.html")

@app.route("/doit", methods=["POST"])
def lets_do_it():

    # increment session["count"]
    session["count"] += 1
    
    users = session['users']
    users.append(f"{request.form['first_name']} {request.form['last_name']}")
    

    return redirect('/')

app.run(debug=True)