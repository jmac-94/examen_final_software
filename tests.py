import unittest as ut
import json
from flask.testing import FlaskClient

from api import app

app.testing = True
client = FlaskClient(app)

class TestPagos(ut.TestCase):
    def test_get_contactos(self):
        '''
            Caso de prueba exitoso:
            Obtiene todos los contactos de de cierto numero
        '''

        response = client.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            {
                '123': 'Luisa',
                '456': 'Andrea'
            }
        )

    def test_pagar_contacto_no_existente(self):
        '''
            Caso de prueba de error:
            Intenta pagar a un contacto que no existe
            en la lista de contactos de la cuenta emisora del pago
        '''

        response = client.get('/billetera/pagar?minumero=21345&numerodestino=1000&valor=50')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"Error": "Cuenta no encontrada"})

    def test_get_historial_no_existente(self):
        '''
            Caso de prueba de error:
            Intenta obtener el historial de una cuenta que no existe
        '''

        response = client.get('/billetera/historial?minumero=1')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"Error": "Cuenta no encontrada"})

    def test_pagar_valor_muy_alto(self):
        '''
            Caso de prueba de error:
            Intenta pagar a un contacto que no existe
            en la lista de contactos de la cuenta emisora del pago
        '''

        response = client.get('/billetera/pagar?minumero=21345&numerodestino=123&valor=50000')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"Error": "Cuenta no encontrada"})

if __name__ == '__main__':
    ut.main()