from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.igekterrexlcotjfvpos:dF3a1Xn8W8XvHQhg@aws-0-us-east-1.pooler.supabase.com:6543/postgres'

db.init_app(app)

class Ropa(db.Model):
    __tablename__ = 'ropa'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(), nullable=False)
    imagen = db.Column(db.String(), nullable=False)

ROPAS = [
    {
        "id": 1,
        "nombre": "Pantalon",
        "precio": 100,
        "descripcion": "Pantalon de mezclilla",
        "imagen": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com.mx%2FLevis-501-Original-Fit-Jeans%2Fdp%2FB0018ON4ZI&psig=AOvVaw0"
    },
    {
        "id": 2,
        "nombre": "Camisa",
        "precio": 200,
        "descripcion": "Camisa de vestir",
        "imagen": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com.mx%2FLevis-501-Original-Fit-Jeans%2Fdp%2FB0018ON4ZI&psig=AOvVaw0"
    },
    {
        "id": 3,
        "nombre": "Playera",
        "precio": 50,
        "descripcion": "Playera de algodon",
        "imagen": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com.mx%2FLevis-501-Original-Fit-Jeans%2Fdp%2FB0018ON4ZI&psig=AOvVaw0"
    },
    {
        "id": 4,
        "nombre": "Chamarra",
        "precio": 300,
        "descripcion": "Chamarra de piel",
        "imagen": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com.mx%2FLevis-501-Original-Fit-Jeans%2Fdp%2FB0018ON4ZI&psig=AOvVaw0"
    },
    {
        "id": 5,
        "nombre": "Sudadera",
        "precio": 150,
        "descripcion": "Sudadera con capucha",
        "imagen": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com.mx%2FLevis-501-Original-Fit-Jeans%2Fdp%2FB0018ON4ZI&psig=AOvVaw0"
    }
]

with app.app_context():
    db.create_all()

    for ropa in ROPAS:
        db.session.add(Ropa(nombre=ropa['nombre'], precio=ropa['precio'], descripcion=ropa['descripcion'], imagen=ropa['imagen']))

    db.session.commit()



@app.route("/")
def hello():
    return render_template('home.html', 
                           ropas=ROPAS)
@app.route("/ropas")
def lista_ropas():
    return jsonify(ROPAS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
