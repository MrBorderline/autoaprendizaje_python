# Clases, Objetos, atributos y metodos.

## Clases
Podemos definir una **clase** vagamente como una **Plantilla** o **modelo** para crear a partir de **ella** ciertos **Objetos**.
 Esta plantilla es la que contiene la ***información; características y capacidades*** que tendrá el objeto que sea creado a partir de ella.

- :exploding_head: **Los objetos creados** a partir de ella estarán **agrupados en esa misma clase**.
- :exploding_head: **Crear un objeto a partir de una clase se denomina instanciar.**

Una clase es un modelo para la creación de objetos. Definimos una clase utilizando la palabra clave class.


```python
class Persona:
    def __init__(self, nombre, edad):  # El método __init__ se llama cuando se crea un nuevo objeto.
        self.nombre = nombre # 'nombre' es un atributo de la clase.
        self.edad = edad # 'edad' es un atributo de la clase.
```

## Objetos
Podemos definir a un objeto como una instancia específica de una clase.

- Puedes pensar en un objeto como una entidad concreta basada en la plantilla de la clase. 
- Estas entidades tienen un **comportamiento**; un **estado**; **almacenan información** y pueden **realizar tareas**.
- Refiriéndonos a **comportamiento** como acciones o capacidades de realizar cambios; y a estados como situación o modo de estar en un momento determinado.
- No necesariamente todos deben derivar de una clase; pueden existir objetos sin que hallan sido creados de una clase en particular. 
- Cada objeto tiene sus propios valores para los atributos definidos en la clase y puede realizar acciones a través de los métodos asociados
>[!NOTE] Un constructor en programación orientada a objetos es un método especial que se llama automáticamente cuando se crea un objeto de una clase. Su función principal es inicializar los atributos del objeto y realizar cualquier configuración necesaria para que el objeto esté en un estado coherente. 

Creamos un objeto llamando al constructor de la clase.





```python
persona1 = Persona("Sebastian", 30)
```

## Atributos y metodos
Los **atributos** son como las características o propiedades de un objeto, mientras que los **métodos** son las acciones que ese objeto puede llevar a cabo.

- Atributo:
Un atributo en programación orientada a objetos es una característica o propiedad asociada a un objeto. Es una variable que pertenece a una clase y define las características de los objetos creados a partir de esa clase. Los atributos representan datos que describen el estado del objeto. Por ejemplo, en una clase Persona, los atributos pueden ser nombre, edad, altura, etc. Cada objeto de la clase Persona tendrá sus propios valores específicos para estos atributos.

>[!NOTE]Los atributos se definen dentro de una clase y se accede a ellos mediante la notación de punto (objeto.atributo).

- Método:
Un método en programación orientada a objetos es una función asociada a una clase o a un objeto. Representa el comportamiento o las acciones que un objeto puede realizar. Los métodos definen las operaciones que pueden realizarse en los objetos de una clase. Por ejemplo, en una clase Automovil, un método podría ser acelerar, que define la acción de aumentar la velocidad del automóvil.
  
>[!NOTE]Los métodos se definen dentro de una clase y toman como primer parámetro el objeto (self) al que se aplica. Se accede a los métodos también mediante la notación de punto (objeto.metodo()).

### Metodos Especiales:

- En Python, existen una serie de métodos especiales que empiezan y terminan con doble guion bajo, como `__init__` y `__str__`. Estos métodos son utilizados para definir comportamientos específicos en las clases y son invocados automáticamente en ciertos momentos. Aquí hay algunos ejemplos de métodos especiales en Python

`__init__(self, ...):`
- Este es el constructor de la clase y se llama automáticamente cuando se crea un nuevo objeto. Se utiliza para inicializar los atributos del objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```
`__str__(self):`
- Este método se llama cuando se utiliza la función str(objeto) y proporciona una representación en forma de cadena del objeto. Es útil para la presentación legible del objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
```

Tambien tenemos algunos como `__len__`, `__getitem__`, `__repr__`, `__add__`, `__del__`, entre otros.

>[!NOTE] https://diveintopython3.net/special-method-names.html

### Finalizacion de ejemplo con codigo y analisis.

```python
class Persona:
    def __init__(self, nombre, edad):  # El método __init__ se llama cuando se crea un nuevo objeto.
        self.nombre = nombre # 'nombre' es un atributo de la clase.
        self.edad = edad # 'edad' es un atributo de la clase.


    def saludar(self): # Metodo "saludar"
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.") # Utilizacion de los atributos "nombre" y "edad"

# Crear un objeto de la clase Persona
persona1 = Persona("Sebastian", 30)

# Acceder al atributo y llamar al método del objeto
print(persona1.nombre)  # Imprimirá "Sebastian"
persona1.saludar()      # Imprimirá "Hola, soy Sebastian y tengo 30 años."
```

Analizamos 
- **nombre** es un **atributo** de la clase Persona. Cuando creamos un objeto de esta clase, especificamos el nombre y se guarda en el **atributo nombre**.

- **"__ init__"** es un **método especial llamado constructor**. Se ejecuta automáticamente cuando se crea un nuevo objeto. En este caso, se utiliza para inicializar el atributo nombre.

- **saludar** es un **método** de la clase Persona que imprime un saludo utilizando el nombre almacenado en el atributo nombre.

- Creamos un **objeto** llamado persona1 y le asignamos el **nombre** "Sebastian".
- Accedemos al **atributo nombre** y llamamos al **método saludar**.