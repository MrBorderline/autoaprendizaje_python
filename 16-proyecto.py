import os

CARPETA = 'contactos/' # Definimos una constante 
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # Revisar que exista la carpeta
    crear_directorio() # llamamos a una funcion dentro de nuestra funcion app
    
    # Mostrar menu de opciones
    mostrar_menu()
    
    # Input del usuario | preguntar que operacion realizar
    preguntar = True
    while preguntar:
        opcion = input('\r\nSeleccione una opcion: \r\n')
        # necesitamos convertir el string (str) a intenger(int)
        opcion = int(opcion)
        
        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False       
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            print('Eliminar Contacto')
            preguntar = False
        elif opcion == 6:
            print('')
            preguntar = False
        else:
            print('Opcion no valida! \r\n')

def agregar_contacto():
    print('..::Escribe los datos para agregar el contacto::..')
    nombre_contacto = input('Nombre del Contacto: \r\n')
    
    #existe = os.path.isfile (CARPETA + nombre_contacto + EXTENSION) # usamos un validador para analizar si el archivo ya existe con os.path.isfile. Similar al validador del directorio os.path.exists
    existe = existe_contacto(nombre_contacto) # utilizo una funcion para validar
    if not existe: # Verificamos que si no existe procesa a realizar nuestra operacion de creacion de usuario.
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # agregamos demas datos
            telefono_contacto = input('Telefono del Contacto: \r\n')
            categoria_contacto = input('Categoria del Contacto: \r\n')
            
            # Instanciamos la clase 
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto) # parametrizamos la clase con las variables de los inputs
            
            # Podriamos simplemente usar las variables de los inputs tambien, para amigarnos usamos las instancias de la pase "Contacto"
            archivo.write('Nombre: ' + contacto.nombre + '\r\n') # nombre_contacto
            archivo.write('Telefono: ' + contacto.telefono + '\r\n') # telefono_contacto
            archivo.write('Categoria: ' + contacto.categoria + '\r\n') # categoria_contacto
            
            # Mostrar mensaje de exito
            print('Contacto creado correctamente! \r\n')
    else:
        print('El contacto ya existe! \r\n')
    app()

def editar_contacto():
    print('..::Edicion de contacto::.. \r\n')
    nombre_anterior = input('Ingresar nombre del Contacto a editar: \r\n')
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo: 
            # Solicitamos al usuario que cargue los nuevos datos
            nombre_contacto = input('Nombre nuevo del Contacto: \r\n')
            telefono_contacto = input('Telefono nuevo del Contacto: \r\n')
            categoria_contacto = input('Categoria nueva del Contacto: \r\n')
            # instanciamos Contacto class
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            # Escribir archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n') # nombre_contacto
            archivo.write('Telefono: ' + contacto.telefono + '\r\n') # telefono_contacto
            archivo.write('Categoria: ' + contacto.categoria + '\r\n') # categoria_contacto
            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    else:
        print('\r\nEse contacto no existe \r\n')
    app()

def mostrar_contacto():
    # Lista archivos en una ruta especifica, en nuestro caso nuestra app trabaja con archivos de un directorio. 
    archivos = os.listdir(CARPETA) 
    # Esto es una comprension de listas y solo 
    archivo_txt = [i for i in archivos if i.endswith(EXTENSION)] # realiza la iteracion y SI el listado termina con la extension .txt lo podremos usar
    
    for i in archivo_txt: # itera sobre archivo_txt anteriormente realizado
        with open(CARPETA + i ) as contacto: # Abre el archivo y lee su contenido por cada elemento de la lista y genera el alias con el nombre "contacto"
            for linea in contacto: # bucle for sobre "contacto" que definimos en la funcion open() del with y asignamos el nombre "linea", podria ser "i", 'elemento' etc... 
                print(linea.rstrip() + '\r') # printeamos 
            # agregamos un separador entre la salida del for
            print('\r\n')

def buscar_contacto():
    nombre = input('Escriba el nombre del contacto que busca: \r\n') # pedimos al usuario que agregue el contacto por stdin
    try: # usa
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('Informacion del contacto \r\n')
            for line in contacto:
                print(line.rstrip())
    except IOError:
        print('El archivo no existe')
        print(IOError)
            

def mostrar_menu():
    print('Seleccione la operacion a realizar')
    print('1- Agregar contacto')
    print('2- Editar contacto ')
    print('3- Ver Contacto')
    print('4- Buscar Contacto')
    print('5- Eliminar Contacto')
    print('6- ')

def crear_directorio(): 
    if not os.path.exists(CARPETA): # usamos if not para validar que sino existe una carpeta con la funcion os.path.exists(nombre_de_la_carpeta)
        os.makedirs(CARPETA) # Si no existe usa os.makedirs(nombre_de_la_carpeta) para crear una

def existe_contacto(nombre):
    return os.path.isfile (CARPETA + nombre + EXTENSION)

app()