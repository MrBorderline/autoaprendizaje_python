lenguajes = ['python','php','javascript','kotlin']

print(lenguajes)

# Los arrays (list) comienzan en la posicion 0
print(lenguajes[0]) #Python stdout

# ordenar array con elemento "sort"
lenguajes.sort() # sort es un metodo que ordena alfabeticamente los strings
print(lenguajes)

# acceder a un elemento dentro del texto
aprendiendo = f'Estoy aprendiendo  {lenguajes[3]}' # para mezclar un STRING con una VARIABLE se utiliza la letra f 
print(aprendiendo)

# Modificar valores de un/a  List/a
lenguajes[2] = 'C#'
print(lenguajes)

# agregar elementos al arreglo / array / List 
lenguajes.append('Ruby')
print(lenguajes)

# eliminar arreglos (list)
del lenguajes[1]
print(lenguajes)

# eliminar de un arreglo (list) el ultimo elemento
lenguajes.pop()
print(lenguajes)

