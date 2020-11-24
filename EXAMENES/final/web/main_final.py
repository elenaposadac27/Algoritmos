from flask import Flask, request, make_response, redirect, render_template, url_for

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route("/")
def home():
   return render_template('home.html')

@app.route("/doctores")
def doctoresRoute():
    return render_template("doctores.html")

@app.route("/pacientes")
def pacientesRoute():
    return render_template("pacientes.html")

@app.route("/conocenos")
def conocenosRoute():
    return render_template("conocenos.html")

@app.route("/contactanos")
def contactanosRoute():
    return render_template("contactanos.html")

@app.route("/curioso")
def curiosoRoute():
    return render_template("curioso.html")

if __name__== "__main__":
    app.run()