from flask import Flask, render_template
app = Flask(__name__)

# localhost:5000
@app.route("/")
def index():
    options = {
        "story": "It was a cloudy and dreary day.  You are leaving the bank.  When suddenly, out of nowhere... A clown appears.",
        "options": [
            {"content": "Pretend you know the clown", "route": "pretend"},
            {"content": "Run away from the clown", "route": "run"}
        ],
        "image": "https://cdn.vox-cdn.com/thumbor/LF-o7juzy4AMUa2p6i8qWaFw4xU=/0x0:2048x1156/1200x800/filters:focal(299x94:625x420)/cdn.vox-cdn.com/uploads/chorus_image/image/49587899/15746767658_8338d05a3e_k.0.jpg"
    }
    return render_template("index.html", choices=options, font_color="yellow")

@app.route("/pretend")
def pretend():
    options = {
        "story": "You awkwardly smile and mention something about the weather.  The clown then starts to juggle machetes and begins to walk toward you.  You are equal parts impressed and terrified",
        "options": [
            {"content": "Snatch a machete out of the air", "route": "machete"},
            {"content": "Run for your life", "route": "run"},
            {"content": "Start a 5 minute standup routine", "route": "standup"}
        ],
        "image": "https://awesomestuff365.com/wp-content/uploads/2016/10/scary-clown-masks.jpg?x12869"
    }
    return render_template("index.html", choices=options, font_color="green")

@app.route("/run")
def run():
    options = {
        "story": "You run fast and hard, sweating under the opressive head of a New Orleans summer.",
         "options": [
            {"content": "Dive into the rank brown waters of the Mississippi", "route": "dive"},
            {"content": "Keep running", "route": "continue"},
        ],
        "option_a": {"content": "Dive into the rank brown waters of the Mississippi", "route": "dive"},
        "option_b": {"content": "Keep running", "route": "continue"},
        "image": "http://www.neworleansrunningtours.com/wp-content/uploads/2014/09/IMG_2615-1038x576.jpg"
    }
    return render_template("index.html", choices=options)

@app.route("/machete")
def machete():
    return "You die.  By way of machete"

@app.route("/dive")
def dive():
    return "You find a big bag of money in the stinky, oily waters.  YOU WIN"

@app.route("/continue")
def keep_running():
    return "You get hit by a bus and die"

@app.route("/standup")
def standup():
    return "The clown reacts badly to your attempt at humor.  You die."

if __name__ == "__main__":
    app.run(debug=True)