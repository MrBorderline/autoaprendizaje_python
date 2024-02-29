nombre = input('Cual es tu nombre: ')
print(nombre)
edad = input('Cuantos años tienes?: ')

edad = int(edad)

if edad >= 18:
    print('Podes votar')
else:
    print('No podes votar todavia ')
    
numero = input('agrega un numero y te digo si es par o inpar: ')

numero = int(numero)

if numero % 2 == 0: # es un metodo donde podemos obtener con 0 o 1 si es par, ya que el residuo debe dar 0 para ser par
    print(f'El numero  {numero} es par')
else:
    print(f'El numero {numero} no es par')
    