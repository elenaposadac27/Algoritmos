from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route("/")
def home():
   return render_template('home.html')

@app.route("/doctors")
def placesRoute():
    return render_template("doctors.html")

@app.route("/services")
def servicessRoute():
    return render_template("services.html")

@app.route("/about")
def aboutRoute():
    return render_template("about.html")

@app.route("/contact")
def contactRoute():
    return render_template("contact.html")

if __name__== "__main__":
    app.run()