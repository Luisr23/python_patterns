# Clase User con Singleton en Python

Este repositorio contiene una implementación de la clase `User` que sigue el patrón Singleton y valida el número de teléfono y el correo electrónico.

## Estructura del Proyecto

    Singleton/
    ├── README.md
    ├── singleton.py
    ├── test_user.py
    └── docs/
        └── singleton.md

- **singleton.py**: Contiene la implementación del Singleton y la clase `User`.
- **test_user.py**: Pruebas unitarias para la clase `User`.
- **docs/**: Documentación del código.
- **README.md**: Este archivo, que proporciona una visión general del proyecto.

## Uso

Para usar la clase `User`, simplemente importa y crea instancias de la clase. Todas las instancias apuntarán a la misma referencia.

```python
from singleton import User

user1 = User("John", "Doe", 30, "123456789", "john.doe@example.com")
user2 = User("Jane", "Smith", 25, "987654321", "jane.smith@example.com")

print(user1 is user2)  # True
print(user1.getName())  # John
print(user2.getName())  # John
```

## Ejecutar Pruebas Unitarias

Para ejecutar las pruebas unitarias, asegúrate de tener Python instalado y luego ejecuta el siguiente comando desde la línea de comandos en el directorio raíz del proyecto:

    python3 -m unittest test_user.py

Esto ejecutará todas las pruebas definidas en el archivo `test_user.py` y mostrará los resultados en la terminal.