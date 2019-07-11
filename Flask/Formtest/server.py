from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    cc = request.form['credit_card']
    amt = request.form['amount']
    # DONT render_template AFTER DB WAS HIT POST!! BAD!!
    return redirect('/puppy')

@app.route('/puppy', methods=["POST", "GET"])
def create_puppy():
    print(request.form)
    return redirect("/")

app.run(debug=True)