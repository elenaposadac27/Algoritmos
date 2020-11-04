from flask import Flask, request, make_response, redirect, render_template

#Se crea un objeto del tipo app que almacenará la aplicación
app = Flask(__name__)

@app.route("/")
def homeRoute():
    return render_template("home.html")

@app.route("/places")
def placesRoute():
    return render_template("places.html")
@app.route("/people")
def peopleRoute():
    return render_template("people.html")
if __name__== "__main__":
    app.run()