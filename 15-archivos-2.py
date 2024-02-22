def app():
    # usamos una funcion de python que nos permite hacer un alias
    # en este caso usamos open(archivo.txt) y no designamos privilegio, ya que por default esta en read ("r") 
    # y le asignamos el valor "archivo", lo que hara es leer el contenido del archivo.txt y almacenar su contenido en "archivo"
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())# la funcion rstrip elimina los saltos de linea en blanco

app()