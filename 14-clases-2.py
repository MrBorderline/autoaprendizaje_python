class Restaurant():
    def __init__(self, nombre, categoria, precio ):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

# Instanciar la clase

restaurant = Restaurant('Catamaranes','Frutos de mar', 30 )
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Las cuartetas','Pizzeria',20)
restaurant2.mostrar_informacion()


