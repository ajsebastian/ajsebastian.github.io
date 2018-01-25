from flask import Flask, render_template

app = Flask(__name__)


# Decorator
@app.route('/')
def index():
    return render_template("main.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/stats')
def stats():
    return render_template("stats.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/forgot')
def forgot():
    return render_template("forgot.html")


if __name__ == "__main__":
    app.run(debug=True)
