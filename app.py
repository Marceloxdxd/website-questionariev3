from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route("/")
def hello():
    return render_template('home.html', 
                           ropas=ROPAS)
@app.route("/ropas")
def lista_ropas():
    return jsonify(ROPAS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
