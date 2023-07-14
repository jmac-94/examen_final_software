from datetime import datetime

class Operacion:
    def __init__(self, numero_origen: str, numero_destino: str, valor: int):
        self.numero_origen = numero_origen
        self.numero_destino = numero_destino
        self.fecha = datetime.now()
        self.valor = valor

class Cuenta:
    def __init__(self, numero: str, nombre: str, saldo: int, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos  # lista de numeros de cuenta en str
        self.pagos_realizados = []  # lista de Operaciones
        self.pagos_recibidos = []  # lista de Operaciones

    def pagar(self, destino: 'Cuenta', valor: int) -> None:
        if (valor <= self.saldo) and (destino.numero in self.contactos):
            operacion = Operacion(self.numero, destino.numero, valor)
            self.pagos_realizados.append(operacion)
            destino.pagos_recibidos.append(operacion)

            self.saldo = self.saldo - valor
        else:
            print("No se pudo realizar la transferencia")
            print()

    def historial(self):
        historial_pagos_realizados = []
        historial_pagos_recibidos = []

        for pago_realizado in self.pagos_realizados:
            historial_pagos_realizados.append({
                'valor': pago_realizado.valor,
                'numero_destino': pago_realizado.numero_destino,
                'fecha': pago_realizado.fecha.strftime('%Y-%m-%d %H:%M:%S')
            })

        for pago_recibido in self.pagos_recibidos:
            historial_pagos_recibidos.append({
                'valor': pago_recibido.valor,
                'numero_origen': pago_recibido.numero_origen,
                'fecha': pago_recibido.fecha.strftime('%Y-%m-%d %H:%M:%S')
            })

        return {
            f'saldo de {self.nombre}': self.saldo,
            'historial_pagos_realizados': historial_pagos_realizados,
            'historial_pagos_recibidos': historial_pagos_recibidos
        }

if __name__ == "__main__":
    cuenta1 = Cuenta('1234', 'Luisa', 1000, ['5678'])
    cuenta2 = Cuenta('5678', 'Juan', 500, ['1234'])

    cuenta2.pagar(cuenta1, 200)
    print(cuenta1.historial())
    print(cuenta2.historial())


    cuenta1.pagar(cuenta2, 1000)
    print(cuenta1.historial())
    print(cuenta2.historial())