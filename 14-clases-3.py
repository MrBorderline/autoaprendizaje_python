# Encapsulamiento es una convencion, si bien no esta definido el metodo de escritura de codigo es tomado de hecho por la comunidad para comprender 
# el codigo. El uso de getters y setters, los encapsulamientos "Default(PUBLIC), PROTECTED y PRIVATE" no brindan una seguridad inquebrantable en el codigo
# pero podemos hacer uso de ellas para generar un codigo facil de leer y operar, definiendo con algunas convenciones de que manera pretendemos 
# tratar los datos

# Definición: El encapsulamiento es el concepto de agrupar los datos (atributos) y los métodos (funciones) que operan en esos datos en una única unidad llamada objeto. 
# Esto oculta la implementación interna de los objetos y solo expone una interfaz para interactuar con ellos.
# En Python: Aunque no hay encapsulamiento estricto, se utilizan convenciones para indicar el nivel de accesibilidad de atributos y 
# métodos (públicos, protegidos, privados).

class Restaurant():
    def __init__(self, nombre, categoria, precio ):
        self.nombre = nombre
        self.categoria = categoria
        ## Encapsulamiento del atributo | Default sin guiones, PROTECTED con un guion bajo (_) PRIVATE usando doble guion bajo (__), 
        self.__precio = precio # al ser seteado de esta forma solo podra ser alimentado mediante un argumento en la llamada de la clase mediante objetos-
        # Sino, debera usarse Getters o Setters
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
        
    # GETTERS / SETTERS - Get = obtiene un valor, SET = agrega un valor 
    def get_precio(self):
        return self.__precio 
    
    def set_precio(self, precio):
        self.__precio = precio # procede a setear el valor obtenido en la llamada de la clase al atributo "precio" y permite que podamos setear 
        # externamente este nuevo valor, de lo contrario, nos informara que es un objeto  u error de sintaxis.

# Instanciar la clase
# En PRIVATE solo toma los valores pasados por sus argumentos
restaurant = Restaurant('Catamaranes','Frutos de mar', 30 ) # Toma en cuenta estos valores
restaurant.mostrar_informacion() # Muestra la informacion previo a SET
restaurant.set_precio(80) # llamamos a la clase Restaurant con el objeto "restaurant" y seteamos mediante el metodo "set_precio" el nuevo valor.
precio = restaurant.get_precio() # definimos una variable con la que pretendemos obtener el dato que nos brinda el metodo "get_precio" del objeto restaurant
print(precio) # Podemos imprimir el objeto "precio"


restaurant2 = Restaurant('Las cuartetas','Pizzeria',20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(30)
precio = restaurant2.get_precio()
print(precio) 


