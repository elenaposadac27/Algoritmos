from flask import Flask, request, make_response, redirect

#Se crea un objeto del tipo app que almacenará la aplicación
app = Flask(__name__)

@app.route("/")
def home():
    user_ip = request.remote_addr
    return f"Hola a todos!!, tu ip es {user_ip}"

if __name__== "__main__":
    app.run()