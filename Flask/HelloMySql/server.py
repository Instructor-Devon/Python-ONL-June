from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    
    mysql = connectToMySQL("mydb")
    result = mysql.query_db("SELECT * FROM users")
    print(result)
    
    return render_template("index.html", users=result)

@app.route("/show/<user_id>")
def show(user_id):

    query = "SELECT * FROM users WHERE id = %(USER_ID)s"
    data = {
        "USER_ID": user_id
    }
    mysql = connectToMySQL("mydb")
    result = mysql.query_db(query, data)

    print(result[0])
    return render_template("show.html", user=result[0])

@app.route("/create", methods=["POST"])
def create():
    
    print(request.form) # post request as a dictionary

    query = "INSERT INTO users (name, location, created_at, updated_at) VALUES (%(nm)s, %(loc)s, NOW(), NOW());"
    data = {
        "nm": request.form["name"],
        "loc": request.form["location"],
    }
    mysql = connectToMySQL("mydb")
    mysql.query_db(query, data)
    return redirect("/")

@app.route("/update/<user_id>", methods=["POST"])
def update(user_id):

    query = "UPDATE users SET name = %(nm)s, location = %(loc)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        "id": user_id,
        "nm": request.form["name"],
        "loc": request.form["location"]
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

if __name__ == "__main__":
    app.run(debug=True)
