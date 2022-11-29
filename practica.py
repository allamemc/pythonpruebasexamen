#crea una clase llamada Producto
#nombre, unidades y precio
#creas un producto camisa, 10, 9.95 de precio
#muestra el nombre de producto por consola

#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

#práctica de sobreescritura.
#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Producto():
    def __init__(self,nombre,unidades,precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
    def infoProducto(self):
        print(f'Datos de su producto: {self.nombre} - {self.unidades} - {self.precio} - {self.unidades*self.precio}')

class Servicio():
    def consultarDetalle(self):
        print('El servicio es básico')

class Estandar(Servicio):
    def consultarDetalle(self):
        print('El servicio es estándar')
class Premium(Servicio):
    def consultarDetalle(self):
        print('El servicio es premium')

camisa=Producto('camisa',10,9.95)
camisa.infoProducto()

x=input('Dime el servicio: ')
match x:
    case 'estandar':
        servicio = Estandar()
        servicio.consultarDetalle()
    case 'premium':
        servicio = Premium()
        servicio.consultarDetalle()
    case _:
        print('No es ningun servicio')


