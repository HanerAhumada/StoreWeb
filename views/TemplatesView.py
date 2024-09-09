from flask import render_template, url_for, redirect, flash, Blueprint

TemplatesView = Blueprint('TemplatesView', __name__)

@TemplatesView.route('/templates/<cat>')
def templates(cat):
    return render_template('Plantillas/plantillas.html');