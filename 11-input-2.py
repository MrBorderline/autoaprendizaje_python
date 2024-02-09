pregunta = ('agrega un numero y te digo si es par o inpar: \r\n')
pregunta += (' Escribe "cerrar" para terminar el programa \r\n')   
preguntar = True

while preguntar: # El while siempre se mantendra ejecutando si es que tenemos un accion que se cumpla 
    numero = input(pregunta)
    if numero == 'cerrar':
        preguntar = False
        print('Gracias por utilizar el programa')
    else:
        numero = int(numero)
        if numero % 2 == 0: # es un metodo donde podemos obtener con 0 o 1 si es par, ya que el residuo debe dar 0 para ser par
            print(f'El numero {numero} es par')
        else:
            print(f'El numero no es par')
    