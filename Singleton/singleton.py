import re

def singleton(cls):
    """
    Crea una instancia singleton de la clase dada.

    Parameters:
        cls (tipo): la clase para crear una instancia singleton.

    Returns:
        función: una función contenedora que devuelve la instancia singleton de la clase.

    """
    instances = {}
    def wrapper(*args, **kwargs):
        """
        Una función contenedora que garantiza que solo se cree y devuelva una instancia de una clase.

        Parámetros:
            *args (Any): lista de argumentos de longitud variable.
            **kwargs (Any): argumentos de palabras clave arbitrarias.

        Returns:
            cls: una instancia de la clase.

        """
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class User(object):    # User = singleton(User)
    
    def __init__(self, name, lastmame, age, phone, email):
        self.setName(name)
        self.setLastName(lastmame)
        self.setAge(age)
        self.setPhone(phone)
        self.setEmail(email)
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setLastName(self, lastmame):
        self.lastmame = lastmame
    
    def getLastmame(self):
        return self.lastmame
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def setPhone(self, phone):
        if not re.fullmatch(r'\d{9}', phone):
            raise ValueError("El número de teléfono debe tener 9 dígitos.")
        self.phone = phone
    
    def getPhone(self):
        return self.phone
    
    def setEmail(self, email):
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Correo electrónico no válido.")
        self.email = email
    
    def getEmail(self):
        return self.email