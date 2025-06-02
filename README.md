# 🔐 Password Security Toolkit

Una herramienta completa de ciberseguridad para generar y analizar contraseñas seguras, desarrollada como parte del estudio de Hacking Ético.

##  📚 Características

### Generador de Contraseñas
- ✅ Generación criptográficamente segura usando `secrets`
- ✅ Parámetros personalizables (longitud, tipos de caracteres)
- ✅ Opción de contraseñas pronunciables
- ✅ Exclusión de caracteres ambiguos
- ✅ Generación masiva de contraseñas

### Analizador de Contraseñas
- ✅ Puntuación de seguridad (0-100)
- ✅ Análisis de entropía
- ✅ Detección de patrones débiles
- ✅ Estimación de tiempo de cracking
- ✅ Verificación contra contraseñas comunes
- ✅ Análisis de tipos de caracteres
- ✅ Feedback específico para mejorar

### Interfaz
- ✅ CLI colorida e intuitiva
- ✅ Modo interactivo completo
- ✅ Argumentos de línea de comandos
- ✅ Análisis masivo desde archivo

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/password-security-toolkit.git
cd password-security-toolkit
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

##  📚 Uso

### Modo Interactivo
```bash
python main.py
```

### Generación Rápida
```bash
# Generar contraseña de 16 caracteres
python main.py -g -l 16

# Generar sin símbolos
python main.py -g --no-symbols
```

### Análisis Rápido
```bash
# Analizar una contraseña específica
python main.py -a "MiContraseña123!"
```

## 📊 Ejemplos de Análisis

### Contraseña Débil
```
───────────────────────────────────────────────────
─ ANÁLISIS DE CONTRASEÑA ─
│ Contraseña: 123456
│ Longitud: 6 caracteres
│ Puntuación: 5/100
│ Fuerza: Muy Débil
│ Entropía: 19.93 bits
│ Tiempo estimado de cracking: Menos de 1 segundo
───────────────────────────────────────────────────

Recomendaciones:
  ❌ Muy corta. Usa al menos 8 caracteres.
  ❌ Añade: mayúsculas, minúsculas, símbolos
  ❌ Evita patrones predecibles (123, abc, qwerty).
  ❌ Contraseña muy común. Usa algo único.
```

### Contraseña Fuerte
```
─────────────────────────────────────────────
─ ANÁLISIS DE CONTRASEÑA ─ 
│ Contraseña: Tr0ub4dor&3
│ Longitud: 11 caracteres
│ Puntuación: 88/100
│ Fuerza: Muy Fuerte
│ Entropía: 72.6 bits
│ Tiempo estimado de cracking: Miles de años
└────────────────────────────────────────────

Recomendaciones:
  ✅ Longitud adecuada.
  ✅ Buena variedad de caracteres.
```

## 🔍 Características del Análisis

### Criterios de Evaluación
- **Longitud**: Mínimo 8 caracteres, recomendado 12+
- **Variedad**: Combinación de mayúsculas, minúsculas, números y símbolos
- **Entropía**: Medida de aleatoriedad e impredecibilidad
- **Patrones**: Detección de secuencias débiles (123, abc, qwerty)
- **Diccionario**: Verificación contra contraseñas comunes

### Patrones Detectados
- Secuencias numéricas (123456, 987654)
- Secuencias alfabéticas (abcdef, zyxwvu)
- Patrones de teclado (qwerty, asdf)
- Repetición excesiva de caracteres (aaa, 111)
- Fechas comunes (1990, 2024)
- Palabras comunes en español e inglés

## 🛡️ Niveles de Seguridad

| Puntuación | Nivel | Color | Descripción |
|------------|-------|-------|-------------|
| 0-29 | Muy Débil | 🔴 Rojo | Vulnerable a ataques básicos |
| 30-49 | Débil | 🟠 Naranja | Fácil de crackear |
| 50-69 | Moderada | 🟡 Amarillo | Resistencia básica |
| 70-84 | Fuerte | 🟢 Verde claro | Buena seguridad |
| 85-100 | Muy Fuerte | 🟢 Verde | Excelente seguridad |

## 🧮 Cálculo de Entropía

La entropía se calcula usando la fórmula:
```
Entropía = longitud × log₂(tamaño_del_conjunto_de_caracteres)
```

**Conjuntos de caracteres:**
- Minúsculas (a-z): 26 caracteres
- Mayúsculas (A-Z): 26 caracteres  
- Números (0-9): 10 caracteres
- Símbolos (!@#$...): ~32 caracteres

## 📈 Estimación de Tiempo de Cracking

Basado en 1 billón de intentos por segundo (GPU moderna):

| Entropía | Tiempo Estimado |
|----------|----------------|
| < 30 bits | Menos de 1 segundo |
| 30-40 bits | Menos de 1 minuto |
| 40-50 bits | Menos de 1 hora |
| 50-60 bits | Menos de 1 día |
| 60-70 bits | Menos de 1 año |
| 70-80 bits | Miles de años |
| > 80 bits | Millones de años |

## 🔧 Funcionalidades Avanzadas

### Análisis Masivo
```bash
# Crear archivo con contraseñas
echo -e "123456\npassword\nMiContraseña123!" > passwords.txt

# Analizar desde archivo (modo interactivo)
python main.py
# Seleccionar opción 3 → opción 2 → passwords.txt
```

### Generación Pronunciable
```python
from generator import PasswordGenerator

gen = PasswordGenerator()
# Genera contraseñas como: "Boto-Keva47", "Nilu-Moxe12"
password = gen.generate_pronounceable(length=12)
```

## 🎓 Propósito Educativo

Esta herramienta fue desarrollada como parte del estudio de **Ciberseguridad y Hacking Ético** para:

- Demostrar la importancia de contraseñas fuertes
- Educar sobre métodos de evaluación de seguridad
- Practicar desarrollo de herramientas de ciberseguridad
- Comprender algoritmos de generación segura
- Analizar patrones de vulnerabilidad comunes

## 🔒 Buenas Prácticas Implementadas

1. **Generación Segura**: Uso de `secrets` en lugar de `random`
2. **Sin Almacenamiento**: Las contraseñas no se guardan
3. **Validación de Entrada**: Verificación de parámetros
4. **Feedback Constructivo**: Consejos específicos de mejora
5. **Detección de Patrones**: Identificación proactiva de debilidades

## 🚨 Advertencias de Seguridad

- ⚠️ No usar contraseñas generadas como ejemplos en sistemas reales
- ⚠️ Esta herramienta es para fines educativos y de auditoría
- ⚠️ Siempre usar generadores de contraseñas de confianza en producción
- ⚠️ No introducir contraseñas reales para análisis en sistemas compartidos

## 🛠️ Estructura del Proyecto

```
password-tool/
├── main.py           # Interfaz principal y CLI
├── generator.py      # Módulo de generación
├── analyzer.py       # Módulo de análisis
├── requirements.txt  # Dependencias
└── README.md        # Documentación
```
## 📜 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 ILANA AMINOFF

Desarrollado como parte del aprendizaje en Ciberseguridad y Hacking Ético.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:
- Abre un issue en GitHub
- Revisa la documentación
- Verifica que tengas las dependencias instaladas

---

**¡Recuerda: Una buena contraseña es tu primera línea de defensa! 🛡️**

**👉 Sígueme para mas contenido de ciberseguridad y herramientas**

## Proyectos destacados

<a href="https://ilanami.github.io/llaNami-ADGuide/">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=ilanami&repo=IlaNami-ADGuide&theme=radical" />
</a>

<a href="https://github.com/ilanami/password-tool">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=ilanami&repo=password-tool&theme=radical" />
</a>

<a href="https://github.com/ilanami/portfolio">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=ilanami&repo=portfolio&theme=radical" />
</a>
