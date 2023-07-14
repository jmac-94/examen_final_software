from flask import Flask, jsonify, request, make_response

from clases import *

app = Flask(__name__)

BD = {
        '21345' : Cuenta('21345', 'Arnaldo', 200, ['123', '456']),
        '123' : Cuenta('123', 'Luisa', 400, ['456']),
        '456' : Cuenta('456', 'Andrea', 300, ['21345'])
}

@app.route('/billetera/contactos')
def get_contactos():
    numero = request.args.get('minumero')

    if numero in BD:
        cuenta = BD[numero]
        contactos = cuenta.contactos
        return jsonify({numero_contacto: BD[numero_contacto].nombre for numero_contacto in contactos})
    else:
        response = jsonify({"Error": "Cuenta no encontrada"})
        response.status_code = 404
        return make_response(response)

@app.route('/billetera/pagar')
def pagar_valor():
    numero = request.args.get('minumero')
    numero_destino = request.args.get('numerodestino')
    valor: int = int(request.args.get('valor'))

    if (numero in BD) and (numero_destino in BD):
        cuenta = BD[numero]
        if (valor <= cuenta.saldo):
            cuenta_destino = BD[numero_destino]
            cuenta.pagar(cuenta_destino, valor)
            return jsonify({"Realizado en": datetime.now()})
        else:
            response = jsonify({"Error": "Cuenta no encontrada"})
            response.status_code = 404
            return make_response(response)
    else:
        response = jsonify({"Error": "Cuenta no encontrada"})
        response.status_code = 404
        return make_response(response)

@app.route('/billetera/historial')
def get_historial():
    numero = request.args.get('minumero')

    if numero in BD:
        cuenta = BD[numero]
        return jsonify(cuenta.historial())
    else:
        response = jsonify({"Error": "Cuenta no encontrada"})
        response.status_code = 404
        return make_response(response)

if __name__ == '__main__':
    app.run()