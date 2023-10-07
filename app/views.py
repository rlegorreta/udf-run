from app import app
from flask import request, jsonify
from flask import render_template


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/api/v1/udf/Calif_Actinver_manual', methods=['GET'])
def api_id0():
    parameters = request.args
    emisora = parameters.get('emisora')
    serie = parameters.get('serie')

    if emisora == "CETES":
        return "A-"
    if emisora == "BONDESD":
        return "B"
    if emisora == "BPAG91":
        if serie == "220428":
            return "B-"
        else:
            return "A-"

    return "C"


@app.route('/api/v1/udf/Resta_importes', methods=['GET'])
def api_id1():
    parameters = request.args
    limpio = parameters.get('importeLimpio')
    sucio = parameters.get('importeSucio')

    if limpio:
        if sucio:
            try:
                impLimpio = float(limpio)
                impSucio = float(sucio)

                return str(impSucio - impLimpio)
            except ValueError:
                return "Alguno del tipos de datos de los parámetro son de un tipo erróneo", 200
        return "Falto especificar el precio", 405
    return "Faltó especificar los títulos", 405


@app.route('/api/v1/udf/LiquidacionUDF', methods=['GET'])
def api_id2():
    parameters = request.args
    liquidacion = parameters.get('liquidacion')

    if liquidacion == "MD":
        return "UDF liquidacón HOY"
    if liquidacion == "24":
        return "UDF liquidacion para mañaña"

    return "Desconozco otra liquidación"


@app.route('/api/v1/udf/TitulosUDF', methods=['GET'])
def api_id3():
    parameters = request.args
    titulos = parameters.get('titulos')

    if titulos:
        try:
            tit = float(titulos)

            if tit > 10:
                return "Son MUCHOS títulos"

            return "Son POCOS tíiulos"

        except ValueError:
            return "Alguno del tipos de datos de los parámetro son de un tipo erróneo", 200
    return "Faltó especificar los títulos", 405


# This REST service create a new UDF from code called from UDFUI micro.service
#
# project UDFRun
# author: rlh
# date: November, 2022
@app.route('/api/v1/udf/newUDF', methods=['GET'])
def api_id00():
    parameters = request.args
    name = parameters.get('name')
    code = parameters.get('code')

    try:
        file = open( './app/' + name + '.py', 'w')
        file.write(code)
    except IOError:
        print('Error in saving the file')

        return 'error:' + IOError.errno
    finally:
        file.close()
        return 'saved'


