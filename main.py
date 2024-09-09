from flask import Flask, render_template
from utils.db import *
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap
from views.TemplatesView import TemplatesView
from views.usuarioView import usarioView
from models import Productos, Usuarios

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_prefixed_env('FLASK')

databasesetting(app)
db.init_app(app)

"""with app.app_context():
    db.drop_all()
    db.create_all()
"""
app.register_blueprint(TemplatesView)
app.register_blueprint(usarioView)

@app.context_processor
def inject_bootstrap():
    return dict(bootstrap=bootstrap)

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
