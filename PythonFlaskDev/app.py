from flask import Flask, render_template, jsonify

app = Flask(__name__)

ROPAS = [
    {
        "id": 1,
        "nombre": "Pantalon",
        "precio": 100,
        "descripcion": "Pantalon de mezclilla"
    },
    {
        "id": 2,
        "nombre": "Camisa",
        "precio": 200,
        "descripcion": "Camisa de vestir"
    },
    {
        "id": 3,
        "nombre": "Playera",
        "precio": 50,
        "descripcion": "Playera de algodon"
    },
    {
        "id": 4,
        "nombre": "Chamarra",
        "precio": 300,
        "descripcion": "Chamarra de piel"
    },
    {
        "id": 5,
        "nombre": "Sudadera",
        "precio": 150,
        "descripcion": "Sudadera con capucha"
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
