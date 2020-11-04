from flask import Flask, request, make_response, redirect, render_template

#Se crea un objeto del tipo app que almacenará la aplicación
app = Flask(__name__)

@app.route("/")
def homeRoute():
    user_ip = request.remote_addr
    response = make_response(redirect("hello"))
    response.set_cookie("ip",user_ip)
    response.set_cookie("perro", "Kira")
    response.set_cookie("nombre", "Elena")
    return response

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")

@app.route("/hello")
def helloRoute():
    perro = request.cookies.get("perro")
    ip = request.cookies.get("ip")
    return render_template("hello.html", mascota = perro, userIP = ip)

@app.route("/nombre")
def nameRoute():
    nombre = request.cookies.get("nombre")
    return render_template("nombre.html", name = nombre)
if __name__== "__main__":
    app.run()