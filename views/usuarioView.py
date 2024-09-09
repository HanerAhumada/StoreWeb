from flask import render_template, url_for, redirect, flash, Blueprint, request
from controller.usuarioController import usuarioController as usuarioController

usarioView = Blueprint('usarioView', __name__)


@usarioView.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('Utils/Login.html');
    elif request.method == "POST":
        redirect("")

@usarioView.route('/registerUser', methods=["GET", "POST"])
def registerUser():
    if request.method == "GET":
        return render_template('Utils/register.html')
    elif request.method == "POST":
        print(request.form)
        redirect("")
