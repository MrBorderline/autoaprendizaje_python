# Usamos el ejemplo de la creacion de una playlist en alguna app de video/musica

playlist = {'nombre': '', 'canciones' : []} # creamos una estructura de un diccionario y dentro de la misma definimos el modelo de claves y elementos
#playlist = {} # definimos el diccionario vario 
#playlist['canciones'] = [] # creacion de lista con key "canciones" sin elementos en diccionario "playlist"

def app():
    agregar_playlist = True # validador para el bucle con while / bandera 
    while agregar_playlist: # si playlist es True ejecutar hasta su modificacion a False
        nombre_playlist = input('Nombre de la playlist? \r\n')
        if nombre_playlist: # si no hay input, la condicion no se cumple y se repetira x cantidad de veces hasta que haya un input
            playlist['nombre'] = nombre_playlist # insertamos en el diccionario "playlist" el valor de "nombre" segun el input 
            # Ya tenemos un nombre para la playlist pasa a false y se termina la ejecucion
            agregar_playlist = False
            # llamamos a una nueva funcion dentro de la funcion app
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True # validador para el bucle while
    while agregar_cancion: # si agregar_cancion es True
        nombre_playlist = playlist['nombre'] # creamos una variable para obtener el valor que se le brindo a playlist['nombre']
        pregunta = f'\r\nAgregar canciones a la playlist "{nombre_playlist}": \r\n'
        pregunta += '*** Escribe "X" para finalizar la carga de canciones \r\n'
        cancion = input(pregunta)
        if cancion == 'X':
            # dejar de agregar items a nuestra lista
            # sabemos que con la condicion afirmativa de que  (if) {cancion} == "X" procedera a determinar el valor "agregar_cancion" en false para cortar el bucle
            agregar_cancion = False 
            # llamada/invocacion funcion 
            mostrar_canciones()
        else:
            #agregar las canciones a la playlist con el metodo append
            playlist['canciones'].append(cancion)

def mostrar_canciones():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('canciones:')
    for cancion in playlist['canciones']:
        print(cancion)
    print(playlist)
    
app()