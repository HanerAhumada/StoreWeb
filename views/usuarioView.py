from flask import render_template, url_for, redirect, flash, Blueprint, request
from controller.usuarioController import usuarioController as usuarioController
usarioView = Blueprint('usarioView', __name__)

usuarioController = usuarioController()


@usarioView.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('Utils/Login.html')
    elif request.method == "POST":
        data = request.form

        # Llamar al método login del controlador
        login_result = usuarioController.login(data)

        if login_result == 'Login exitoso':
            return redirect("/")  # Redirigir al home si el login fue exitoso
        else:
            return redirect("/login")


@usarioView.route('/registerUser', methods=["GET", "POST"])
def registerUser():
    if request.method == "GET":
        return render_template('Utils/register.html')
    elif request.method == "POST":
        usuarioController.POST(request.form)
        return redirect("/")
