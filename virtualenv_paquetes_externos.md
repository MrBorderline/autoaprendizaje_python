
## Creacion de entorno virtual (encapsulamiento)
virtualenv es una herramienta en Python que se utiliza para crear entornos virtuales. Un entorno virtual es una copia aislada del intérprete de Python y de la librería estándar, lo que permite trabajar en proyectos con dependencias específicas sin afectar al entorno global de Python.



### Instalacion, desinstalacion y exportacion de paquetes en python

```bash
# Instalacion de paquetes simples
pip install Flask # sintax pip install <Nombre_Paquete>
```

```bash
# Instalacion de paquetes multiples mediante listado de paquetes
# debemos tener un archivo .txt agregado los paquetes linea x linea
pip install -r req.txt # al pip install le agregamos el flag -r seguido del txt
```

```bash
# Eliminacion de paquetes instalados
pip uninstall Flask # Desinstalacion por paquete
# O
pip uninstall -r req.txt # Desinstalacion por listado de paquetes
```

```bash
# Si realizamos la instalacion de diferentes paquetes en nuestro proyecto y no tenemos idea de cuales fueron con sus respectiva versiones, podemos exportarlo de la siguiente manera
pip freeze
```

### Instalacion y uso de virtualenv

```bash
# Instalacion del paquete virtualenv con pip
pip install virtualenv
```

```bash
# Creacion de entorno virtual. Esto genera una carpeta en el directorio raiz de tu proyecto con el nombre que le brindes
# sintaxis virtualenv <NOMBRE>
virtualenv venv  # Esto creará un nuevo directorio llamado venv que contendrá el entorno virtual
```

```bash
# activacion de entorno virtual 
source venv/bin/activate
```
>[!NOTE] Recordar que la activacion realiza un entorno virtual encapsulado, para instalar paquetes y no realizarlo de manera global. Esto nos brinda la posibilidad de "jugar" con diferentes versiones de paquetes ante la necesidad que se presente sin tener problemas con otros proyectos.


```bash
# desactivacion del entorno virtual
deactivate # esto se puede realizar en cualquier momento.
```

- [Volver al README](README.md)