# import json
# lista = {'id':'1',
#          'name':'maxi',
#          'edad':'35',
#          'sexo':'masculino',
#          'aptitudes':['enojado','perseverante','lindo'],
#          'gustos':['marihuana','sexo infantil','cojerme a tu vieja']
#         }

# json_string = json.dumps(lista)
# print(json_string)


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Método genérico para todos los animales

class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Meow!"

def hacer_sonar_animal(animal):
    return animal.hacer_sonido()

perro = Perro("Fido")
gato = Gato("Whiskers")

print(hacer_sonar_animal(perro))  # Salida: Woof!
print(hacer_sonar_animal(gato))   # Salida: Meow!

