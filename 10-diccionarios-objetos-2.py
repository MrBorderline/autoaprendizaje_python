# Iniciar diccionario vacio
jugador = {}

# agregar un elemento al diccionario u objeto
# unir un "jugador"
jugador['nombre'] = 'Maxi'
jugador['puntaje'] = 0
print(jugador)

# incrementar puntaje
jugador['puntaje'] = 100
print(jugador)


# acceder a un valor
# usando el metodo .get nos permite que sino existe podamos
# agregar un mensaje mas legible
# CLAVE : VALOR 
# print(objeto.get('CLAVE', 'mensaje si CLAVE no existe o no esta definido, False'))
print(jugador.get('puntaje', 'No existe ese valor'))

#Iterar sobre el diccionario

for key, value in jugador.items():
    print(f'{key}: {value}')


# eliminacion de claves 
# del jugador['nombre']
# del jugador['puntaje']
# print(jugador)

