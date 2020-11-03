from flask import Flask, request, make_response, redirect, render_template

#Se crea un objeto del tipo app que almacenará la aplicación
app = Flask(__name__)

@app.route("/")
def homeRoute():
    response = make_response(redirect("home"))
    response.set_cookie("place1", "Dubrovnik, Croacia")
    response.set_cookie("place2", "Orlando, Estados Unidos")
    response.set_cookie("place3", "Paris, Francia")
    response.set_cookie("place4", "Madrid, España")
    response.set_cookie("place5", "Medellín, Colombia")
    response.set_cookie("person1", "Mamá")
    response.set_cookie("person2", "Papá")
    response.set_cookie("person3", "Hermanas")
    response.set_cookie("person4", "Abuelos")
    response.set_cookie("person5", "Nicolás")
    return render_template("home.html")

@app.route("/places")
def placesRoute():
    place1 = request.cookies.get("place1")
    place2 = request.cookies.get("place2")
    place3 = request.cookies.get("place3")
    place4 = request.cookies.get("place4")
    place5 = request.cookies.get("place5")
    return render_template("places.html", lugar1 = place1, lugar2 = place2, lugar3 = place3, lugar4 = place4, lugar5 = place5)

@app.route("/people")
def peopleRoute():
    person1 = request.cookies.get("person1")
    person2 = request.cookies.get("person2")
    person3 = request.cookies.get("person3")
    person4 = request.cookies.get("person4")
    person5 = request.cookies.get("person5")
    return render_template("people.html", persona1 = person1, persona2 = person2, persona3 = person3, persona4 = person4, persona5 = person5)
if __name__== "__main__":
    app.run()