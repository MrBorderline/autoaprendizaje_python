# Modulos y Paquetes 

## Modulos

Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos.


### Creacion de un modulo 
Para ejemplificarlo vamos a generar un modulo de operaciones aritmeticas designando un archivo con el nombre **aritmetica.py** con el siguiente contenido:

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
```

Para utilizar el modulo antes mencionado, lo podemos importar en un script, por ejemplo **app.py** con un **import** sumado del nombre del archivo que definimos el modulo sin el **.py**.
Por ejemplo:

### Importacion de modulo
```python
import aritmetica
```

Con esto ya tendremos el modulo para ser utilizado llamando a las funciones que definimos con anterioridad.

### Utilizacion de funcione del modulo con notacion de punto
```python
import aritmetica

print(aritmetica.sumar(3, 5))
```

>[!NOTE]
La notación de punto en Python se utiliza para acceder a funciones, variables o clases dentro de módulos, paquetes u objetos. La sintaxis general es objeto.atributo o objeto.metodo().

Como podemos ver en el ejemplo, al importar "aritmetica" hacemos un print llamando a  modulo.funcion pasandole parametros ```(aritmetica.sumar(a, b))```. 

>[!WARNING]Tener en cuenta que se debe usar la funcion con la notacion de punto, de lo contrario tendremos un error similar al siguiente:

```bash
Traceback (most recent call last):
  File "/home/user/autoaprendizaje_python/app.py", line 3, in <module>
    print(sumar(3, 5))
NameError: name 'sumar' is not defined. Did you mean: 'super'?
```

Esto es porque aunque importemos un modulo, los objetos del modulo son propios del mismo y debemos informarle a python que queremos usar este modulo en particular con la notacion de punto.

Otro tipo de importacion es la de sus objetos, como podemos ver en el siguiente ejemplo:

```python
from aritmetica import sumar

print(sumar(10, 10))
```

En este ejemplo podemos visualizar que se le informa a python que desde el modulo "aritmetica" importe el objeto "sumar" que esta definido en el modulo "aritmetica.py" y como vemos no tenemos que usar la notacion de punto ```(aritmetica.sumar(a, b))```.

Asi mismo tambien podemos obtener un listado de objetos del modulo:

```python
from aritmetica import sumar, restar, mult, div

print(sumar(7, 5))
print(restar(7, 5))
print(mult(7, 5))
print(div(7, 5))
```

Podremos tambien simplificar la importacion de todos sus objetos sin especificar un listado como el ejemplo anterior:

```python
from aritmetica import *
```

## Paquetes
Un **paquete** es una carpeta que contiene varios módulos. 
Para este ejemplo usamos una carpeta que llamaremos **op_matematica**, dentro de la misma creamos un archivo `__init__.py`. La presencia de este ultimo indica que el directorio **op_matematica** debe ser tratado como un paquete.

>[!NOTE] 
El archivo __init__.py puede estar vacio o bien tambien puede tener codigo ejecutable, pero su existencia es lo que convierte al directorio en un paquete.

Utilizaremos [el modulo aritmetica](#creacion-de-un-modulo) que hemos definido al principio del documento y lo crearemos dentro de la carpeta **op_matematica**. 

Nuestro paquete tendra una estructura como la siguiente:
```bash
op_matematica
├── aritmetica.py
├── __init__.py
```

Esta seria la estructura que tendremos, teniendo en cuenta que nuestra app esta en el directorio raiz y el paquete (carpetea op_matematica) estaria al mismo nivel. 

```bash
.
├── app.py
├── op_matematica
│   ├── aritmetica.py
│   ├── __init__.py
```

Para acceder al paquete es similar a la importacion de un modulo, como ya sabemos para la importacion de modulos utilizamos `import <nombre_modulo>`  y utilizamos notacion de punto  y tambien podemos importar sus funciones como por ejemplo `sumar`,`restar`,`mult`, etc. 

>[!NOTE]
En Python, la notación de punto es comúnmente utilizada para acceder a módulos, funciones o variables dentro de paquetes. La sintaxis general es paquete.modulo.funcion() o paquete.modulo.variable.


Teniendo el paquete **op_matematica**, dentro de el un modulo **aritmetica** accedemos a la funcion `sumar` y utilizamos la notacion de puntos.

```python
from op_matematicas import aritmetica

resultado = aritmetica.sumar(3, 5)
print(resultado)
```

Sin embargo, también podemos utilizar la palabra clave **from** para importar funciones específicas directamente, evitando la notación de punto al llamarlas:

```python
from op_matematicas.aritmetica import sumar

resultado = sumar(3, 5)
print(resultado)
```

En este caso, solo se importa la función `sumar` del módulo `aritmetica` del paquete `op_matematicas`. Se puede elegir la opción que prefieras según tus necesidades y **preferencias de estilo de código**.

>[!IMPORTANT]
Es importante tener en cuenta que, aunque la notación de punto es la forma estándar y legible de acceder a funciones en paquetes, hay casos donde usar from puede hacer que tu código sea más claro, especialmente si solo necesitas unas pocas funciones de un módulo específico.


## Resumen 

__Paquetes__:

- Son directorios que contienen módulos y un archivo especial llamado __init__.py.
- Organizan y estructuran el código en jerarquías.
- Permiten agrupar módulos relacionados en un espacio de nombres común.
- Ayudan a evitar conflictos de nombres al organizar el código de manera más clara.

__Módulos__:

- Son archivos de Python que contienen definiciones y declaraciones.
- Permiten organizar y reutilizar código de manera efectiva.
- Pueden contener funciones, variables, clases y código ejecutable.
- Facilitan la modularidad y mantenimiento del código al dividirlo en componentes más pequeños y manejables.

__Notación de Punto__:

- Utilizada para acceder a funciones, variables o clases dentro de módulos o paquetes.
- Sintaxis: objeto.atributo o objeto.metodo().
- Proporciona un medio claro para especificar el alcance y la ubicación de un componente en la jerarquía del código.
- Permite evitar conflictos de nombres y organizar el código de manera estructurada.

En resumen, los paquetes son directorios que contienen módulos, los módulos son archivos que contienen código, y la notación de punto se utiliza para acceder a funciones, variables o clases dentro de módulos o paquetes, proporcionando estructura y organización al código.