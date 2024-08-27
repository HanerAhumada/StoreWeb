from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config.from_prefixed_env('FLASK')

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
