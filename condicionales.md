# Condicionales

Las condicionales en programación son estructuras que permiten ejecutar ciertos bloques de código basados en la evaluación de una condición. En Python, las condicionales se implementan principalmente a través de las palabras clave `if`, `else`, y `elif` (abreviatura de "else if").

## If

La instrucción if se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es:

```python
if condicion:
    # Código a ejecutar si la condición es verdadera
```
Ejemplo:

```python
# el código dentro del bloque if se ejecutará porque la condición (edad >= 18) es verdadera.
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
```

## Else
La instrucción `else` se utiliza junto con `if` para ejecutar un bloque de código si la condición en el if es falsa. La sintaxis es:

```python
if condicion:
    # Código a ejecutar si la condición es verdadera
else:
    # Código a ejecutar si la condición es falsa
```

Ejemplo:

```python
# si la edad es menor de 18, se ejecutará el bloque de código dentro del else
edad = 15
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

## Elif
La instrucción `elif` se utiliza para comprobar condiciones adicionales después de un `if`. Se evaluará en orden y el bloque asociado al primer `elif` (o al `else` si todos los `elif` anteriores son falsos) cuya condición sea verdadera se ejecutará. La sintaxis es:

```python
if condicion1:
    # Código a ejecutar si la condición1 es verdadera
elif condicion2:
    # Código a ejecutar si la condicion1 es falsa y la condicion2 es verdadera
else:
    # Código a ejecutar si todas las condiciones anteriores son falsas
```

Ejemplo:

```python
# evalúan condiciones múltiples y se ejecuta el bloque de código asociado a la primera condición verdadera.
puntuacion = 75
if puntuacion >= 90:
    print("Excelente.")
elif puntuacion >= 70:
    print("Buena.")
else:
    print("Aprobado.")
```

Las condicionales son esenciales para tomar decisiones en programas y controlar el flujo de ejecución. Permiten que tu código sea más flexible y reactivo a diferentes situaciones.

- [Volver al README](README.md)