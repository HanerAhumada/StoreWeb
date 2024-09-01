from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_prefixed_env('FLASK')
db = SQLAlchemy(app)

@app.context_processor
def inject_bootstrap():
    return dict(bootstrap=bootstrap)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)