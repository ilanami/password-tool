import re
import math
from collections import Counter

class PasswordAnalyzer:
    def __init__(self):
        # Patrones comunes débiles
        self.weak_patterns = [
            r'123+',  # Secuencias numéricas
            r'abc+',  # Secuencias alfabéticas
            r'qwerty',  # Teclado
            r'password',  # Palabra común
            r'admin',  # Palabras de administrador
            r'user',
            r'guest',
            r'(\w)\1{2,}',  # Repetición de caracteres
        ]
        
        # Contraseñas muy comunes
        self.common_passwords = {
            'password', '123456', '12345678', 'qwerty', 'abc123', 
            'password123', 'admin', 'letmein', 'welcome', 'monkey',
            'dragon', 'master', 'sunshine', 'iloveyou', 'princess'
        }
        
        # Palabras comunes en español
        self.common_spanish = {
            'contraseña', 'clave', 'secreto', 'amor', 'familia',
            'casa', 'trabajo', 'dinero', 'vida', 'corazon'
        }
    
    def analyze_password(self, password):
        """
        Análisis completo de una contraseña
        """
        if not password:
            return self._empty_analysis()
            
        analysis = {
            'password': password,
            'length': len(password),
            'score': 0,
            'strength': '',
            'feedback': [],
            'patterns': self._detect_patterns(password),
            'character_sets': self._analyze_character_sets(password),
            'entropy': self._calculate_entropy(password),
            'crack_time': self._estimate_crack_time(password),
            'is_common': self._is_common_password(password)
        }
        
        # Calcular puntuación total
        analysis['score'] = self._calculate_score(analysis)
        analysis['strength'] = self._get_strength_level(analysis['score'])
        analysis['feedback'] = self._generate_feedback(analysis)
        
        return analysis
    
    def _analyze_character_sets(self, password):
        """
        Analiza qué tipos de caracteres contiene la contraseña
        """
        sets = {
            'lowercase': bool(re.search(r'[a-z]', password)),
            'uppercase': bool(re.search(r'[A-Z]', password)),
            'digits': bool(re.search(r'[0-9]', password)),
            'symbols': bool(re.search(r'[^a-zA-Z0-9]', password)),
            'count': 0
        }
        
        sets['count'] = sum([sets['lowercase'], sets['uppercase'], 
                           sets['digits'], sets['symbols']])
        
        return sets
    
    def _detect_patterns(self, password):
        """
        Detecta patrones débiles en la contraseña
        """
        detected = []
        pwd_lower = password.lower()
        
        for pattern in self.weak_patterns:
            if re.search(pattern, pwd_lower):
                detected.append(pattern)
        
        # Detectar fechas (YYYY, MM/DD/YYYY, etc.)
        if re.search(r'(19|20)\d{2}', password):
            detected.append('date_pattern')
            
        # Detectar secuencias de teclado
        keyboard_patterns = ['qwerty', 'asdf', '1234', 'zxcv']
        for pattern in keyboard_patterns:
            if pattern in pwd_lower:
                detected.append(f'keyboard_{pattern}')
        
        return detected
    
    def _calculate_entropy(self, password):
        """
        Calcula la entropía de la contraseña
        """
        if not password:
            return 0
            
        # Determinar el espacio de caracteres
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            charset_size += 32  # Símbolos comunes
            
        if charset_size == 0:
            return 0
            
        # Entropía = log2(charset_size^length)
        entropy = len(password) * math.log2(charset_size)
        return round(entropy, 2)
    
    def _estimate_crack_time(self, password):
        """
        Estima el tiempo necesario para crackear la contraseña
        """
        if not password:
            return "Instantáneo"
            
        entropy = self._calculate_entropy(password)
        
        # Asumiendo 1 billón de intentos por segundo (GPU moderna)
        attempts_per_second = 1e12
        
        # Tiempo promedio = 2^(entropy-1) / attempts_per_second
        if entropy < 30:
            return "Menos de 1 segundo"
        elif entropy < 40:
            return "Menos de 1 minuto"
        elif entropy < 50:
            return "Menos de 1 hora"
        elif entropy < 60:
            return "Menos de 1 día"
        elif entropy < 70:
            return "Menos de 1 año"
        elif entropy < 80:
            return "Miles de años"
        else:
            return "Millones de años"
    
    def _is_common_password(self, password):
        """
        Verifica si es una contraseña común
        """
        pwd_lower = password.lower()
        
        # Verificar contraseñas exactas
        if pwd_lower in self.common_passwords or pwd_lower in self.common_spanish:
            return True
            
        # Verificar variaciones simples (añadir números al final)
        base_pwd = re.sub(r'\d+$', '', pwd_lower)
        if base_pwd in self.common_passwords or base_pwd in self.common_spanish:
            return True
            
        return False
    
    def _calculate_score(self, analysis):
        """
        Calcula la puntuación total de la contraseña (0-100)
        """
        score = 0
        
        # Puntos por longitud (máximo 25 puntos)
        length_score = min(25, analysis['length'] * 2)
        score += length_score
        
        # Puntos por variedad de caracteres (máximo 25 puntos)
        char_variety = analysis['character_sets']['count'] * 6
        score += min(25, char_variety)
        
        # Puntos por entropía (máximo 30 puntos)
        entropy_score = min(30, analysis['entropy'] / 3)
        score += entropy_score
        
        # Puntos base por no ser común (máximo 20 puntos)
        if not analysis['is_common']:
            score += 20
        
        # Penalizaciones por patrones débiles
        pattern_penalty = len(analysis['patterns']) * 5
        score -= min(30, pattern_penalty)
        
        # Asegurar que esté entre 0-100
        return max(0, min(100, round(score)))
    
    def _get_strength_level(self, score):
        """
        Determina el nivel de fuerza basado en la puntuación
        """
        if score < 30:
            return "Muy Débil"
        elif score < 50:
            return "Débil"
        elif score < 70:
            return "Moderada"
        elif score < 85:
            return "Fuerte"
        else:
            return "Muy Fuerte"
    
    def _generate_feedback(self, analysis):
        """
        Genera retroalimentación específica para mejorar la contraseña
        """
        feedback = []
        
        # Feedback por longitud
        if analysis['length'] < 8:
            feedback.append("❌ Muy corta. Usa al menos 8 caracteres.")
        elif analysis['length'] < 12:
            feedback.append("⚠️  Considera usar al menos 12 caracteres.")
        else:
            feedback.append("✅ Longitud adecuada.")
        
        # Feedback por variedad de caracteres
        char_sets = analysis['character_sets']
        if char_sets['count'] < 3:
            missing = []
            if not char_sets['uppercase']:
                missing.append("mayúsculas")
            if not char_sets['lowercase']:
                missing.append("minúsculas")
            if not char_sets['digits']:
                missing.append("números")
            if not char_sets['symbols']:
                missing.append("símbolos")
            feedback.append(f"❌ Añade: {', '.join(missing)}")
        else:
            feedback.append("✅ Buena variedad de caracteres.")
        
        # Feedback por patrones débiles
        if analysis['patterns']:
            feedback.append("❌ Evita patrones predecibles (123, abc, qwerty).")
        
        # Feedback por contraseñas comunes
        if analysis['is_common']:
            feedback.append("❌ Contraseña muy común. Usa algo único.")
        
        return feedback
    
    def _empty_analysis(self):
        """
        Retorna análisis vacío para contraseñas vacías
        """
        return {
            'password': '',
            'length': 0,
            'score': 0,
            'strength': 'Sin Contraseña',
            'feedback': ['❌ La contraseña no puede estar vacía.'],
            'patterns': [],
            'character_sets': {'lowercase': False, 'uppercase': False, 
                             'digits': False, 'symbols': False, 'count': 0},
            'entropy': 0,
            'crack_time': 'Instantáneo',
            'is_common': True
        }