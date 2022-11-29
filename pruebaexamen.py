#crea una función que nos permita:
#pide la ciudad a donde viajar.
#indica la fecha de salida
#selecciona la estancia
#muestra un detalle al cliente sobre su reserva.
#ciudad destino - checkin/checkout -
#si la estancia es superior a 5 días, descuento es true
#los datos se almacenan en el tipo de dato correcto. 1/5
#gestiona los tipos de entrada son validos 1/5
#muestra por consola el detalle de la reserva calculado la fecha de salida
#calculando la fecha de salida y el descuento 1/5
#un fichero de texto 1/5
#utilizar programacion funcional 1/5

from datetime import *

#definicion de la funcion
def reservar():

    #formulario de registro / entrada
    ciudad=input('dime tu ciudad de destino: ')#almacen string
    fecha=input('indica la fecha de entrada (dd/mm/yyyy): ')
    dias=int(input('indica los dias de estancia: '))

    #cuidado por que todas las variables son string por el retorno de input
    fecha_entrada=datetime.strptime(fecha, '%d/%m/%Y')
    fecha_salida = fecha_entrada + timedelta(days=dias)
    descuento=False
    if dias > 5:
        descuento=True

    print(fecha_entrada)
    print(fecha_salida)
    print(ciudad)
    print(dias)
    print(descuento)
reservar()