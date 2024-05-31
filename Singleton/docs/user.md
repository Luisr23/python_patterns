# Documentación de la Clase User

## Clase User

La clase `User` implementa el patrón Singleton y permite almacenar la información de un usuario, incluyendo validaciones para el número de teléfono y el correo electrónico.

### Métodos

#### `__init__(self, name, lastmame, age, phone, email)`

Constructor de la clase User.

- **name**: Nombre del usuario.
- **lastmame**: Apellido del usuario.
- **age**: Edad del usuario.
- **phone**: Número de teléfono del usuario (debe tener 9 dígitos).
- **email**: Correo electrónico del usuario (debe ser un correo válido).

#### `setName(self, name)`

Establece el nombre del usuario.

- **name**: Nombre del usuario.

#### `getName(self)`

Obtiene el nombre del usuario.

- **Returns**: Nombre del usuario.

#### `setLastName(self, lastmame)`

Establece el apellido del usuario.

- **lastmame**: Apellido del usuario.

#### `getLastmame(self)`

Obtiene el apellido del usuario.

- **Returns**: Apellido del usuario.

#### `setAge(self, age)`

Establece la edad del usuario.

- **age**: Edad del usuario.

#### `getAge(self)`

Obtiene la edad del usuario.

- **Returns**: Edad del usuario.

#### `setPhone(self, phone)`

Establece el número de teléfono del usuario.

- **phone**: Número de teléfono del usuario (debe tener 9 dígitos).

#### `getPhone(self)`

Obtiene el número de teléfono del usuario.

- **Returns**: Número de teléfono del usuario.

#### `setEmail(self, email)`

Establece el correo electrónico del usuario.

- **email**: Correo electrónico del usuario (debe ser un correo válido).

#### `getEmail(self)`

Obtiene el correo electrónico del usuario.

- **Returns**: Correo electrónico del usuario.
