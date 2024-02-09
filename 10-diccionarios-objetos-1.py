# Creacion de objeto 
musica = {
    'artista' : 'Iron Maiden',
    'tema' : 'The Evil That Man Do',
    'lanzamiento' : '1995',
    'likes' : '30000',
    'estilo' : 'metal',
    }

# acceder a los elementos del diccionario/objeto 
print(musica) # el objeto completo
print(musica['artista']) # el value de la key "artista"
print(musica['tema']) # el value de la key "tema"

# Mezclar con string 
# NOTA sintax error sino le asignamos una variable al valor que queremos utilizar

#Ejemplo con error:  ya que no se puede iterar entre un objeto de esta manera
 #print(f'Estoy escuchando {musica['artista']}' )

#Debemos crear una variable que nos permita almacenar el resultado para luego utilizarlo

artista = musica['artista']
print(f'Estoy escuchando a {artista}')

# Agregar nuevos valores sino existen 
musica['playlist'] = 'Heavy Metal'

# reemplazar si existente  
musica['tema'] = 'The Number of the beast'

# eliminar si existente  
del musica['likes'] 

print(musica)
