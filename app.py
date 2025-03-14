from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.routes import app_routes, cargar_datos_iniciales
from models.db import db
from config import Config  

app = Flask(__name__, template_folder="views")

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(app_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        cargar_datos_iniciales()
    app.run(debug=True)
