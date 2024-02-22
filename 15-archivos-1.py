def app():
    # crear archivo txt
    archivo = open('archivo.txt', 'w') # usamos open() y pasamos 2 parametros: Nombre del archivo y permisos, en este caso "w" que sino existe lo crea
    
    for i in range(0, 20):
        archivo.write('Esta es la linea ' + str(i) + '\r\n')
    # cerramos el archivo - evitamos consumos en memoria si llegamos a tener gran caudal de archivos abiertos.
    archivo.close()

app()