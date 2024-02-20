class Restaurant():
    def agregar_restaurant(self, nombre ):
        self.nombre = nombre
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

# Instanciar la clase

restaurant = Restaurant()
restaurant.agregar_restaurant('Panchos 69')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Tucan ')
restaurant2.mostrar_informacion()

