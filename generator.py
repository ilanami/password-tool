import secrets
import string
import random

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%&*()_+-=[]{}|;:,.<>?"
        
    def generate_password(self, length=12, use_uppercase=True, use_lowercase=True, 
                         use_digits=True, use_symbols=True, exclude_ambiguous=False):
        """
        Genera una contraseña segura con parámetros personalizables
        """
        if length < 4:
            raise ValueError("La longitud mínima debe ser 4 caracteres")
        
        charset = ""
        required_chars = []
        
        # Construir conjunto de caracteres disponibles
        if use_lowercase:
            charset += self.lowercase
            required_chars.append(secrets.choice(self.lowercase))
            
        if use_uppercase:
            charset += self.uppercase
            required_chars.append(secrets.choice(self.uppercase))
            
        if use_digits:
            charset += self.digits
            required_chars.append(secrets.choice(self.digits))
            
        if use_symbols:
            charset += self.symbols
            required_chars.append(secrets.choice(self.symbols))
        
        if not charset:
            raise ValueError("Debe seleccionar al menos un tipo de carácter")
        
        # Excluir caracteres ambiguos si se solicita
        if exclude_ambiguous:
            ambiguous = "0O1lI|"
            charset = ''.join(c for c in charset if c not in ambiguous)
            
        # Generar contraseña
        password = required_chars.copy()
        
        # Completar con caracteres aleatorios
        for _ in range(length - len(required_chars)):
            password.append(secrets.choice(charset))
            
        # Mezclar la contraseña
        random.shuffle(password)
        
        return ''.join(password)
    
    def generate_pronounceable(self, length=12, separator='-'):
        """
        Genera una contraseña pronunciable usando palabras simples
        """
        consonants = "bcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"
        
        words = []
        current_length = 0
        target_word_length = 4
        
        while current_length < length:
            word = ""
            for i in range(target_word_length):
                if i % 2 == 0:  # Consonante
                    word += secrets.choice(consonants)
                else:  # Vocal
                    word += secrets.choice(vowels)
            
            # Capitalizar primera letra aleatoriamente
            if secrets.choice([True, False]):
                word = word.capitalize()
                
            # Añadir número aleatorio ocasionalmente
            if secrets.choice([True, False]):
                word += str(secrets.randbelow(100))
                
            words.append(word)
            current_length += len(word) + len(separator)
            
            if current_length >= length:
                break
                
        result = separator.join(words)
        
        # Ajustar longitud si es necesario
        if len(result) > length:
            result = result[:length]
        elif len(result) < length:
            # Añadir caracteres adicionales
            result += secrets.choice(self.symbols) + str(secrets.randbelow(10))
            
        return result[:length]
    
    def generate_multiple(self, count=5, **kwargs):
        """
        Genera múltiples contraseñas
        """
        passwords = []
        for _ in range(count):
            passwords.append(self.generate_password(**kwargs))
        return passwords