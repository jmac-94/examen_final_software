# examen_final_software

## Pregunta 3

En primer lugar, en el código de "clases.py" se debería agregar una variable "monto_transferido_dia" que determine cuánto monto es lo que la persona lleva transferido en un dia. Además, se debería reiniciar esta variable cada día al valor 0.

En los métodos al momento de pagar si es que el pago es exitoso se debe aumentar el valor correspondiente del pago a la variable "monto_transferido_dia". Además, se debe agregar una validación de que si la variable "monto_transferido_dia" de la Cuenta ya excedió el máximo de 200 soles que no permita hacer la transferencia.

Se podría agregar dos casos de prueba extra. Uno exitoso que determine que una persona pueda pagar a otra que está en sus contactos cierto monto sin sobrepasar la cantidad de 200 soles. Por otro lado, se puede agregar un caso de prueba de error en donde se intente pagar y la variable monto_transferido_dia ya haya sobrepasado el límite de 200 soles.

Siempre al realizar cambios existe el riesgo de "romper" algo que ya funciona. En este caso, hay la posibilidad de malograr el método "pagar" de la clase Cuenta si es que no se toman las decisiones o medidas necesarias para que todo funcione correctamente.
