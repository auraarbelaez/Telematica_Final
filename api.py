import flask
import pandas as pd

app = flask.Flask(__name__)

@app.route('/sensores_nivel')
def sensores_nivel():
    data = flask.request.args
    url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json"
    try:
        captura_web = pd.read_json(url, convert_dates='True')
        if data.get('Contraseña') == '0000':
            return captura_web.to_dict()
        else:
            return 'Usuario incorrecto'
    except Exception as e:
        return f"Error al obtener los datos: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)