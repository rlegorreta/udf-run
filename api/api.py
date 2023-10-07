import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

test = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Prueba de un API en Phyton</h1><p>Este es un prototipo de UDF.</p>"


@app.route('/api/v1/udf/calificacionGAFs', methods=['GET'])
def calificacionGAF():
    return jsonify(test)


@app.route('/api/v1/udf/calificacionGAF', methods=['GET'])
def api_id():
    parameters = request.args
    titulos = parameters.get('titulos')
    precio = parameters.get('precio')

    if titulos:
        if precio:
            try:
                titles = int(titulos)
                price = float(precio)

                return "<p> El monto es " + str(titles * price) + "</p>", 200
            except ValueError:
                return "Alguno del tipos de datos de los parámetro es ilegal", 405
        return "Falto especificar el precio", 405
    return "faltó especificar los títulos", 405


app.run()
