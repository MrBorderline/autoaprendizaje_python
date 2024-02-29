# Loops For y While

## For

El bucle for en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena o rango) o cualquier objeto iterable. Su sintaxis básica es:

```python
for variable in iterable:
    # Cuerpo del bucle
    # Se ejecuta para cada elemento en el iterable
    # ...
```
 Ejemplo:

```python
# Este bucle imprime cada elemento de la lista frutas.

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# output
manzana
banana
cereza
```
## While
El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. Su sintaxis básica es:

```python
while condicion:
    # Cuerpo del bucle
    # Se ejecuta mientras la condición sea verdadera
    # ...
```
Ejemplo:

```python
# Este bucle imprime las iteraciones mientras el contador sea menor que 5.

contador = 0
while contador < 5:
    print("Iteración:", contador)
    contador += 1

#output
0
1
2
3
4
```

Notas Importantes:

- En un bucle for, la variable de iteración toma el valor de cada elemento en el iterable en cada iteración.
- En un bucle while, el código dentro del bucle se ejecuta mientras la condición sea verdadera.
- Es importante evitar bucles infinitos asegurándote de que la condición en un bucle while eventualmente sea falsa, para ello se usa `contador` para la evaluacion de si la condicion es `True` o `False`