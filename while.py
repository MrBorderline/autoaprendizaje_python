#  WHILE Se utiliza para repetir un bloque de código mientras una condición sea verdadera.
#  FOR Se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena, etc.) o cualquier objeto iterable
count = 0

while count < 5:
    if count <= 2:
        print(f'hola mundo {count}')
    else:
        break
    count += 1