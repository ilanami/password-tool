#!/usr/bin/env python3
"""
Generador y Analizador de Contraseñas - Herramienta de Ciberseguridad
Autor: [Tu nombre]
"""

import argparse
import sys
from colorama import init, Fore, Style, Back
from generator import PasswordGenerator
from analyzer import PasswordAnalyzer

# Inicializar colorama para Windows
init()

class PasswordTool:
    def __init__(self):
        self.generator = PasswordGenerator()
        self.analyzer = PasswordAnalyzer()
        
    def print_banner(self):
        """
        Muestra el banner de la herramienta
        """
        banner = f"""
{Fore.CYAN}{'='*59}
              🔐 PASSWORD SECURITY TOOLKIT 🔐              
                                                           
    Generador y Analizador de Contraseñas Seguras         
                  Hacking Ético v1.0                      
{'='*59}{Style.RESET_ALL}
        """
        print(banner)
    
    def print_menu(self):
        """
        Muestra el menú principal
        """
        menu = f"""
{Fore.YELLOW}─── OPCIONES DISPONIBLES ───
1. Generar contraseña
2. Analizar contraseña
3. Análisis masivo
4. Configuración
5. Salir
{'─'*28}{Style.RESET_ALL}
        """
        print(menu)
    
    def get_color_by_strength(self, strength):
        """
        Retorna el color apropiado según la fuerza de la contraseña
        """
        colors = {
            'Muy Débil': Fore.RED,
            'Débil': Fore.LIGHTRED_EX,
            'Moderada': Fore.YELLOW,
            'Fuerte': Fore.LIGHTGREEN_EX,
            'Muy Fuerte': Fore.GREEN
        }
        return colors.get(strength, Fore.WHITE)
    
    def display_analysis(self, analysis):
        """
        Muestra el análisis de una contraseña de forma bonita
        """
        color = self.get_color_by_strength(analysis['strength'])
        
        print(f"\n{Fore.CYAN}─── ANÁLISIS DE CONTRASEÑA ───{Style.RESET_ALL}")
        print(f"Contraseña: {Fore.WHITE}{analysis['password']}{Style.RESET_ALL}")
        print(f"Longitud: {analysis['length']} caracteres")
        print(f"Puntuación: {color}{analysis['score']}/100{Style.RESET_ALL}")
        print(f"Fuerza: {color}{analysis['strength']}{Style.RESET_ALL}")
        print(f"Entropía: {analysis['entropy']} bits")
        print(f"Tiempo estimado de cracking: {analysis['crack_time']}")
        print(f"{Fore.CYAN}{'─' * 30}{Style.RESET_ALL}")
        
        # Mostrar tipos de caracteres
        char_sets = analysis['character_sets']
        print(f"\n{Fore.MAGENTA}─── Tipos de caracteres ───{Style.RESET_ALL}")
        print(f"  Minúsculas: {'✅' if char_sets['lowercase'] else '❌'}")
        print(f"  Mayúsculas: {'✅' if char_sets['uppercase'] else '❌'}")
        print(f"  Números: {'✅' if char_sets['digits'] else '❌'}")
        print(f"  Símbolos: {'✅' if char_sets['symbols'] else '❌'}")
        
        # Mostrar patrones detectados
        if analysis['patterns']:
            print(f"\n{Fore.RED}⚠️  Patrones débiles detectados:{Style.RESET_ALL}")
            for pattern in analysis['patterns']:
                print(f"  • {pattern}")
        
        # Mostrar feedback
        print(f"\n{Fore.MAGENTA}─── Recomendaciones ───{Style.RESET_ALL}")
        for feedback in analysis['feedback']:
            print(f"  {feedback}")
    
    def generate_password_interactive(self):
        """
        Interfaz interactiva para generar contraseñas
        """
        print(f"\n{Fore.CYAN}─── GENERADOR DE CONTRASEÑAS ───{Style.RESET_ALL}")
        
        try:
            length = int(input("Longitud de la contraseña (8-128): ") or "12")
            if length < 8 or length > 128:
                print(f"{Fore.RED}❌ Longitud debe estar entre 8 y 128 caracteres{Style.RESET_ALL}")
                return
                
            print("\nTipos de caracteres a incluir:")
            use_uppercase = input("¿Incluir mayúsculas? (S/n): ").lower() != 'n'
            use_lowercase = input("¿Incluir minúsculas? (S/n): ").lower() != 'n'
            use_digits = input("¿Incluir números? (S/n): ").lower() != 'n'
            use_symbols = input("¿Incluir símbolos? (S/n): ").lower() != 'n'
            exclude_ambiguous = input("¿Excluir caracteres ambiguos (0,O,1,l)? (s/N): ").lower() == 's'
            
            count = int(input("¿Cuántas contraseñas generar? (1-10): ") or "1")
            count = max(1, min(10, count))
            
            print(f"\n{Fore.GREEN}🔑 Contraseñas generadas:{Style.RESET_ALL}")
            
            for i in range(count):
                password = self.generator.generate_password(
                    length=length,
                    use_uppercase=use_uppercase,
                    use_lowercase=use_lowercase,
                    use_digits=use_digits,
                    use_symbols=use_symbols,
                    exclude_ambiguous=exclude_ambiguous
                )
                
                # Analizar automáticamente
                analysis = self.analyzer.analyze_password(password)
                color = self.get_color_by_strength(analysis['strength'])
                
                print(f"{i+1}. {Fore.WHITE}{password}{Style.RESET_ALL} "
                     f"({color}{analysis['strength']}{Style.RESET_ALL} - "
                     f"{analysis['score']}/100)")
            
            # Opción para analizar una contraseña específica
            choice = input(f"\n¿Analizar alguna contraseña en detalle? (número/n): ")
            if choice.isdigit() and 1 <= int(choice) <= count:
                idx = int(choice) - 1
                passwords = []
                for i in range(count):
                    pwd = self.generator.generate_password(
                        length=length, use_uppercase=use_uppercase,
                        use_lowercase=use_lowercase, use_digits=use_digits,
                        use_symbols=use_symbols, exclude_ambiguous=exclude_ambiguous
                    )
                    passwords.append(pwd)
                
                analysis = self.analyzer.analyze_password(passwords[idx])
                self.display_analysis(analysis)
                
        except ValueError as e:
            print(f"{Fore.RED}❌ Error: Valor inválido{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
    
    def analyze_password_interactive(self):
        """
        Interfaz interactiva para analizar contraseñas
        """
        print(f"\n{Fore.CYAN}─── ANALIZADOR DE CONTRASEÑAS ───{Style.RESET_ALL}")
        
        password = input("Ingresa la contraseña a analizar: ")
        
        if not password:
            print(f"{Fore.RED}❌ No se ingresó ninguna contraseña{Style.RESET_ALL}")
            return
        
        analysis = self.analyzer.analyze_password(password)
        self.display_analysis(analysis)
    
    def mass_analysis(self):
        """
        Análisis masivo de contraseñas desde archivo o lista
        """
        print(f"\n{Fore.CYAN}─── ANÁLISIS MASIVO ───{Style.RESET_ALL}")
        print("1. Ingresar contraseñas manualmente")
        print("2. Cargar desde archivo")
        print("3. Probar contraseñas comunes")
        
        choice = input("Selecciona una opción (1-3): ")
        
        passwords = []
        
        if choice == '1':
            print("Ingresa contraseñas (una por línea, línea vacía para terminar):")
            while True:
                pwd = input("Contraseña: ")
                if not pwd:
                    break
                passwords.append(pwd)
                
        elif choice == '2':
            filename = input("Nombre del archivo: ")
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    passwords = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"{Fore.RED}❌ Archivo no encontrado{Style.RESET_ALL}")
                return
            except Exception as e:
                print(f"{Fore.RED}❌ Error leyendo archivo: {str(e)}{Style.RESET_ALL}")
                return
                
        elif choice == '3':
            passwords = ['123456', 'password', 'admin', 'qwerty', 'abc123',
                        'password123', 'contraseña', 'letmein', 'welcome',
                        'Myp@ssw0rd!2024']
        
        if not passwords:
            print(f"{Fore.RED}❌ No hay contraseñas para analizar{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}📊 Analizando {len(passwords)} contraseñas...{Style.RESET_ALL}\n")
        
        results = []
        for password in passwords:
            analysis = self.analyzer.analyze_password(password)
            results.append(analysis)
        
        # Mostrar resumen
        print(f"{Fore.CYAN}─── RESUMEN DEL ANÁLISIS ───{Style.RESET_ALL}")
        
        strength_counts = {}
        for result in results:
            strength = result['strength']
            strength_counts[strength] = strength_counts.get(strength, 0) + 1
        
        for strength, count in strength_counts.items():
            color = self.get_color_by_strength(strength)
            print(f"{color}{strength:12}{Style.RESET_ALL}: {count:2} contraseñas")
        
        print(f"{Fore.CYAN}{'─' * 28}{Style.RESET_ALL}")
        
        # Mostrar detalles si se solicita
        if input("\n¿Ver análisis detallado? (s/N): ").lower() == 's':
            for i, result in enumerate(results, 1):
                print(f"\n{Fore.YELLOW}--- Contraseña {i} ---{Style.RESET_ALL}")
                self.display_analysis(result)
    
    def run_interactive(self):
        """
        Ejecuta la interfaz interactiva
        """
        self.print_banner()
        
        while True:
            self.print_menu()
            choice = input(f"\n{Fore.CYAN}Selecciona una opción: {Style.RESET_ALL}")
            
            if choice == '1':
                self.generate_password_interactive()
            elif choice == '2':
                self.analyze_password_interactive()
            elif choice == '3':
                self.mass_analysis()
            elif choice == '4':
                print(f"{Fore.YELLOW}⚙️  Configuración - Próximamente{Style.RESET_ALL}")
            elif choice == '5':
                print(f"{Fore.GREEN}👋 ¡Hasta luego! Mantente seguro.{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}❌ Opción inválida{Style.RESET_ALL}")
            
            input(f"\n{Fore.CYAN}Presiona Enter para continuar...{Style.RESET_ALL}")

def main():
    """
    Función principal con argumentos de línea de comandos
    """
    parser = argparse.ArgumentParser(description='Generador y Analizador de Contraseñas')
    parser.add_argument('-g', '--generate', action='store_true', 
                       help='Generar contraseña rápida')
    parser.add_argument('-a', '--analyze', type=str, 
                       help='Analizar contraseña específica')
    parser.add_argument('-l', '--length', type=int, default=12,
                       help='Longitud de contraseña a generar')
    parser.add_argument('--no-symbols', action='store_true',
                       help='No incluir símbolos en generación')
    
    args = parser.parse_args()
    tool = PasswordTool()
    
    if args.generate:
        # Modo rápido de generación
        generator = PasswordGenerator()
        password = generator.generate_password(
            length=args.length,
            use_symbols=not args.no_symbols
        )
        analyzer = PasswordAnalyzer()
        analysis = analyzer.analyze_password(password)
        
        print(f"Contraseña: {password}")
        print(f"Fuerza: {analysis['strength']} ({analysis['score']}/100)")
        
    elif args.analyze:
        # Modo rápido de análisis
        analyzer = PasswordAnalyzer()
        analysis = analyzer.analyze_password(args.analyze)
        tool.display_analysis(analysis)
    else:
        # Modo interactivo
        tool.run_interactive()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Operación cancelada por el usuario{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error inesperado: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)