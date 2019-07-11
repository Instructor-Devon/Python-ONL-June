from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "lol"

EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    
    mysql = connectToMySQL("mydb")
    result = mysql.query_db("SELECT * FROM users")
    # [{"column": row_value}]

    blogs = connectToMySQL("mydb").query_db("SELECT blogs.id, topic, content, name, blogs.created_at FROM blogs JOIN users ON blogs.user_id = users.id")

    return render_template("dashboard.html", users=result, blogs=blogs)
    

@app.route("/show/<user_id>")
def show(user_id):

    query = "SELECT * FROM users WHERE id = %(USER_ID)s"
    data = {
        "USER_ID": user_id
    }
    mysql = connectToMySQL("mydb")
    result = mysql.query_db(query, data)

    blogs = connectToMySQL("mydb").query_db("SELECT * FROM blogs WHERE user_id = %(USER_ID)s", data)


    return render_template("show.html", user=result[0], blogs=blogs)

@app.route("/create", methods=["POST"])
def create():

    # CHECK FOR VALID INPUTS

    # Check for empty inputs
    errors = []
    if(request.form["name"] == ""):
        errors.append("Name field is required")

    if(request.form["email"] == ""):
        errors.append("Email field is required")

    # check for valid email address
    elif not (EMAIL_MATCH.match(request.form["email"])):
        errors.append("Invalid email address")

    if(len(request.form["password"]) < 8):
        errors.append("Password must be 8 characters or more")

    # password and confirm password match!
    if request.form["password"] != request.form["confirm"]:
        errors.append("Passwords do not match")

    # ensure that email is unique
    email_data = {
        "em": request.form["email"]
    }
    has_email = connectToMySQL("mydb").query_db("SELECT id FROM users WHERE email = %(em)s", email_data)
    if len(has_email) > 0:
        errors.append("Email already in use! (did you forget your password?)")

    if errors:
        for error in errors:
            flash(error)
        return render_template("index.html", name=request.form["name"], email=request.form["email"])
    else:
        hashed_pw = bcrypt.generate_password_hash(request.form["password"])
        query = "INSERT INTO users (name, email, password) VALUES (%(nm)s, %(em)s, %(pw)s);"
        data = {
            "nm": request.form["name"],
            "em": request.form["email"],
            "pw": hashed_pw
        }
        mysql = connectToMySQL("mydb")
        print(mysql.query_db(query, data))
        # IF INSERT => id of new thing

        return redirect("/home")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():

    # LOGIN VALIDATIONS (ARE you who you say you are)
    # email, make sure its in the db
    email_data = {
        "em": request.form["email"]
    }
    user_check = connectToMySQL("mydb").query_db("SELECT id, password FROM users WHERE email = %(em)s", email_data)
    if len(user_check) == 0:
        flash("Invalid Email/Password")
        return redirect("/")

    user = user_check[0]
    # if email IS in the DB, make sure password provided matches password in DB
    correct_password = bcrypt.check_password_hash(user["password"], request.form["password"])
    if not correct_password:
        flash("Invalid Email/Password")
        return redirect("/")




    # if user passes both checks: we will "log" them in

    session["user_id"] = user["id"]
    # TODO: for Wednesday

    return redirect("/home")

@app.route("/update/<user_id>", methods=["POST"])
def update(user_id):

    query = "UPDATE users SET name = %(nm)s, email = %(em)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        "id": user_id,
        "nm": request.form["name"],
        "em": request.form["email"]
    }

    mysql = connectToMySQL("mydb")
    mysql.query_db(query, data)

    return redirect("/")

@app.route("/delete/<user_id>")
def delete(user_id):

    query = "DELETE FROM users WHERE id = %(id)s"
    
    mysql = connectToMySQL("mydb")
    mysql.query_db(query, {"id": user_id})

    return redirect("/")

# BLOG STUFF

@app.route("/new")
def new_blog():
    return render_template("newblog.html")

@app.route("/blog", methods=["POST"])
def blog():

    # TODO: (LATER) VALIDATIONS HERE

    query = "INSERT INTO blogs (topic, content, user_id) VALUES (%(top)s, %(con)s, %(uid)s)"
    data = {
        "top": request.form["topic"],
        "con": request.form["blog"],
        "uid": session["user_id"]
    }
    connectToMySQL("mydb").query_db(query, data)

    return redirect("/home")

if __name__ == "__main__":
    app.run(debug=True)

