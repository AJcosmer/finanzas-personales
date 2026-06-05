from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return {
        "mensaje": "API Finanzas Personales"
    }

if __name__ == "__main__":
    app.run(debug=True)
