# Polimorfismos:Definición: El polimorfismo permite que un objeto se comporte de múltiples formas. 
# En el contexto de la POO, esto puede manifestarse a través de la capacidad de diferentes clases de tener métodos con el mismo nombre, pero con implementaciones específicas para cada clase.
# En Python: Se logra mediante la definición de métodos con el mismo nombre en diferentes clases y la capacidad de sobrescribir métodos en las subclases.

class Restaurant():
    def __init__(self, nombre, categoria, precio ):
        self.nombre = nombre
        self.categoria = categoria
        # volvemos el atributo a Public eliminando los guiones de self.precio (anteriormente self.__precio)
        # ya que si no lo modificamos nos aparecera que es un objeto pero no nos permitira operar con el
        self.precio = precio 
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')
        
    def get_precio(self):
        return self.precio 
    
    def set_precio(self, precio):
        self.precio = precio 
        
# Crear clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca ): 
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
    # Reescribimos un metodo  (debe llamarse igual si cambia se toma como un nuevo metodo)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')
    # agregar un metodo que solo exista en hotel
    def get_alberca(self):
        return self.alberca
        
hotel = Hotel('la carlistas', '5 estrellas', 100, 'SI') 
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)