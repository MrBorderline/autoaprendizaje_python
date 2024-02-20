# Herencia: Permite que una clase herede las propiedades y métodos de otra clase. Esto fomenta la reutilización de código 
# y la creación de jerarquías de clases, donde una clase más específica (subclase) puede heredar características de una clase 
# más general (superclase).

class Restaurant():
    def __init__(self, nombre, categoria, precio ):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
        
    def get_precio(self):
        return self.__precio 
    
    def set_precio(self, precio):
        self.__precio = precio 
        
# Crear clase hijo de Restaurant
class Hotel(Restaurant): # creamos una clase Hotel heredando propiedades y metodo de Restaurant
    def __init__(self, nombre, categoria, precio ): 
        # se utiliza la función super() para llamar al método __init__ de la clase padre (Restaurant). 
        # Esto inicializa las propiedades de la clase Hotel con los valores proporcionados para nombre, categoria, y precio. 
        # En otras palabras, está reutilizando el constructor de la clase Restaurant para evitar duplicar código.
        super().__init__(nombre, categoria, precio) 
        
hotel = Hotel('la carlistas', '5 estrellas', 100) 
hotel.mostrar_informacion()