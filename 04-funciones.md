# Funciones
**Definición:** Una función es un bloque de código reutilizable que realiza una tarea específica. Puedes definir funciones con la palabra clave def.
 
```python
 def nombre_func():
``` 
>[!NOTE] 
Se debe tener presente que luego de la funcion debe estar identado para que sea parte de la funcion, de no ser asi se ejecutara por fuera de la funcion o bien algun problema de sintaxis 

```python
def saludar(nombre):
    print("Hola, " + nombre + "!")
```

**Llamada:** Para ejecutar el código dentro de una función, necesitas llamar a la función.

```python
saludar("Juan") 
```

**Parámetros:** Las funciones pueden aceptar parámetros que son valores proporcionados durante la llamada de la función.

```python
def suma(a, b):
    return a + b

resultado = suma(3, 4)
```


```python
def nombre_funcion(parametro_1, parametros_2)
    print(f'{parametro_1} y {parametro_2}')

nombre_funcion('parametros 1', 'parametros 2')
```

**Retorno:** Pueden o no devolver un valor usando la palabra clave return.

```python
def cuadrado(x):
    return x * x
```

```python
def informacion(nombre):
    return nombre

empleado = informacion('maxi')
print(empleado)
```

# Metodos

**Definición:** Un método es similar a una función, pero está asociado con un objeto y se llama en ese objeto. En Python, los métodos son funciones que pertenecen a un objeto y están vinculados a él.

```python
texto = "Hola, mundo!"
longitud = len(texto)
```
En este ejemplo, `len` es un método que pertenece al tipo de datos `str` (cadena de texto).


resultado:
```shell
>>> texto = 'hola mundo'
>>> longitud = len(texto)
>>> print(longitud)
10
```

**Llamada:** Los métodos se llaman en un objeto utilizando la notación de punto.

```python
lista = [1, 2, 3]
lista.append(4)
```
resultado:
```shell
>>> lista = [1,2,3]
>>> lista.append(4)
>>> print(lista)
[1, 2, 3, 4]
```
 `append` es un método que pertenece a la clase `list`(array/arreglo)

**Parámetros:** Al igual que las funciones, los métodos pueden aceptar parámetros.

```python
texto = "Hola, mundo!"
posicion = texto.find("mundo")
```
`find` es un método que acepta un argumento en este caso.

resultado:
```python
>>> texto = "Hola, mundo!"
>>> posicion = texto.find("mundo")
>>> print(posicion)
6
```
**Retorno:** Los métodos también pueden o no devolver un valor

```python
lista = [1, 2, 3]
ultimo_elemento = lista.pop()
```
`pop` es un método que devuelve el último elemento de la lista y lo elimina.
