from flask import Flask, render_template

app = Flask(__name__)

# listen for requests at localhost:5000/
# localhost:5000/
@app.route("/")
def index():
    dudes = ["Jack", "Justin", "Sebastian", "Devon"]

    return render_template("index.html", users=dudes, number=5)

# localhost:5000/fun
@app.route("/fun")
def fun():
    return "This is fun!"

# 127.0.0.1
# localhost to listen on port 5000
app.run(debug=True)