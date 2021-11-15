from flask import Flask, request, redirect, render_template
from main import app

@app.route('/')
def paginaInicio():
    return render_template('/index.html')           #Redireccionar a la vista principal del proyecto

@app.route('/registro.html', methods = ["GET", "POST"])
def registrar():
    if request.method == "GET":
        return render_template('registro.html')
    if request.method == "POST":
        try:
            nombres = request.form["nombre"]
            correo = request.form["correo"]                           #Redireccionar al registro
            key = request.form["pass"]
            keyConfirm = request.form["repass"]
            print("Nombre:", nombres,"\nCorreo: ", correo, "\nKey: ", key)
            return render_template('index.html')
        except:
            print("Error recuperando datos")
            return render_template('registro.html')

@app.route('/acerca.html')
def paginaAcerca():
    return render_template('acerca.html')               #Redireccionar a "Acerca de"

@app.route('/contacto.html')
def paginaContacto():
    return render_template('contacto.html')             #Redireccionar a "Contacto"

@app.route('/preguntas.html')
def paginaPreguntas():
    return render_template('preguntas.html')            #Redireccionar a "Preguntas"

@app.route('/infowiki.html')
def paginaInfo():
    return render_template('infowiki.html')             #Redireccionar a "Info wiki"