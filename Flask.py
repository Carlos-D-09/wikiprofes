from flask import Flask, request, redirect, render_template
from main import app

@app.route('/')
def paginaInicio():
    return render_template('/index.html')

@app.route('/registro.html', methods = ["POST"])
def registrar():
    if request.method == "GET":
        return render_template('registro.html')

@app.route('/acerca.html')
def paginaAcerca():
    return render_template('acerca.html')


#Metodo para el registro de un usuario
# if request.method == "POST":
#     try:
#         nombres = request.form["nombre"]
#         correo = request.form["correo"]
#         key = request.form["pass"]
#         keyConfirm = request.form["repass"]
#         print("Nombre:", nombres,"\nCorreo: ", correo, "\nKey: ", key)
#         return render_template('index.html')
#     except:
#         print("Error recuperando datos")
#         return render_template('registro.html')

