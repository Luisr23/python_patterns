import unittest
from singleton import User

class TestUser(unittest.TestCase):
    def test_singleton(self):
        """
        Prueba  comportamiento singleton de la clase Usuario.

        Esta función crea dos instancias de la clase Usuario con diferentes atributos y
        afirma que son la misma instancia. También afirma que el atributo de nombre de
        ambos casos es "John".

        Parameters:
            - self: La instancia de la clase TestUser.

        Returns:
            None
        """
        user1 = User("John", "Doe", 30, "123456789", "john.doe@example.com")
        user2 = User("Jane", "Smith", 25, "987654321", "jane.smith@example.com")
        
        self.assertIs(user1, user2) 
        self.assertEqual(user1.getName(), "John")
        self.assertEqual(user2.getName(), "John")
        
    def test_phone_validation(self):
        """
        Prueba de validación de números de teléfono en la clase Usuario.

        Este caso de prueba verifica que se genera una excepción cuando un número de teléfono con un
        Se pasa un formato no válido al constructor del usuario. También comprueba que el correcto
        El número de teléfono se devuelve cuando se pasa un número de teléfono válido.

        Parameters:
        - self: la instancia de la clase TestUser.

        Devoluciones:
            None
        """
        with self.assertRaises(ValueError):
            User("John", "Doe", 30, "1234567", "john.doe@example.com")
        
        user = User("John", "Doe", 30, "123456789", "john.doe@example.com")
        self.assertEqual(user.getPhone(), "123456789")
        
    def test_email_validation(self):
        """
        Prueba de validación de correo electrónico de la clase Usuario.

        Este caso de prueba verifica que se genera un ValueError cuando se pasa un correo electrónico no válido al constructor del usuario.
        También verifica que se devuelva el correo electrónico correcto cuando se pasa un correo electrónico válido.

        Parámetros:
        self (TestCase): la instancia del caso de prueba actual.

        Devoluciones:
        Ninguno
        """
        with self.assertRaises(ValueError):
            User("John", "Doe", 30, "123456789", "invalid-email")
        
        user = User("John", "Doe", 30, "123456789", "john.doe@example.com")
        self.assertEqual(user.getEmail(), "john.doe@example.com")

if __name__ == "__main__":
    unittest.main()
