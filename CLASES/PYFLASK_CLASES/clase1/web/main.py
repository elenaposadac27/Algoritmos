from flask import Flask, request, make_response, redirect, render_template

#Se crea un objeto del tipo app que almacenará la aplicación
app = Flask(__name__)

@app.route("/")
def homeRoute():
    user_ip = request.remote_addr
    response = make_response(redirect("hello"))
    response.set_cookie("ip",user_ip)
    response.set_cookie("perro", "Kira")
    return response

@app.route("/hello")
def helloRoute():
    perro = request.cookies.get("perro")
    ip = request.cookies.get("ip")
    return render_template("hello.html", mascota = perro, userIP = ip)

if __name__== "__main__":
    app.run()