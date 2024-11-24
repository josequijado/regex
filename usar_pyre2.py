import re2

class RegexHandler:
    """
    Clase responsable de manejar operaciones relacionadas con expresiones regulares utilizando la biblioteca Pyre2.
    Este diseño cumple con el principio de responsabilidad única (SRP) al separar las operaciones de expresiones regulares 
    del resto de la lógica de la aplicación.
    """
    
    def __init__(self, pattern: str):
        """
        Inicializa un objeto RegexHandler con un patrón específico.
        
        Args:
            pattern (str): Patrón de expresión regular a utilizar.
        
        Raises:
            re2.error: Si el patrón es inválido, se lanza una excepción.
        """
        self.pattern = pattern
        try:
            # Compilamos el patrón para verificar su validez y mejorar el rendimiento
            self.compiled_pattern = re2.compile(pattern)
        except re2.error as e:
            raise ValueError(f"Patrón inválido: {e}")

    def search(self, text: str):
        """
        Busca la primera coincidencia del patrón en el texto.
        
        Args:
            text (str): Texto donde buscar el patrón.
        
        Returns:
            re2.Match: Objeto de coincidencia si se encuentra; None en caso contrario.
        """
        return self.compiled_pattern.search(text)

    def find_all(self, text: str):
        """
        Encuentra todas las coincidencias del patrón en el texto.
        
        Args:
            text (str): Texto donde buscar las coincidencias.
        
        Returns:
            list[str]: Lista de coincidencias encontradas.
        """
        return self.compiled_pattern.findall(text)

    def replace(self, text: str, replacement: str):
        """
        Reemplaza todas las coincidencias del patrón en el texto por un texto dado.
        
        Args:
            text (str): Texto original.
            replacement (str): Texto para reemplazar las coincidencias.
        
        Returns:
            str: Texto con las coincidencias reemplazadas.
        """
        return self.compiled_pattern.sub(replacement, text)


class PatternValidator:
    """
    Clase encargada de validar datos de entrada utilizando patrones predefinidos.
    Este diseño sigue el principio de inversión de dependencia (DIP), ya que depende de la abstracción `RegexHandler`
    en lugar de depender directamente de Pyre2.
    """

    def __init__(self):
        """
        Inicializa el validador con patrones predefinidos.
        """
        # Patrones predefinidos
        self.email_handler = RegexHandler(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        self.date_handler = RegexHandler(r'\b\d{4}-\d{2}-\d{2}\b')  # Formato AAAA-MM-DD
        self.number_handler = RegexHandler(r'\b\d+\b')  # Números enteros

    def validate_email(self, email: str):
        """
        Valida si una cadena es un correo electrónico válido.
        
        Args:
            email (str): Cadena a validar.
        
        Returns:
            bool: True si es un correo electrónico válido, False en caso contrario.
        """
        return bool(self.email_handler.search(email))

    def extract_dates(self, text: str):
        """
        Extrae todas las fechas en formato AAAA-MM-DD del texto.
        
        Args:
            text (str): Texto de entrada.
        
        Returns:
            list[str]: Lista de fechas encontradas.
        """
        return self.date_handler.find_all(text)

    def count_numbers(self, text: str):
        """
        Cuenta la cantidad de números enteros en el texto.
        
        Args:
            text (str): Texto de entrada.
        
        Returns:
            int: Cantidad de números encontrados.
        """
        return len(self.number_handler.find_all(text))


# Clase principal para ejecutar los ejemplos
class Pyre2ExampleRunner:
    """
    Clase principal que ilustra el uso de Pyre2 en un entorno estructurado y orientado a objetos.
    Sigue el principio de responsabilidad única al encargarse únicamente de coordinar las operaciones.
    """

    def __init__(self):
        """
        Inicializa los componentes necesarios para ejecutar los ejemplos.
        """
        self.validator = PatternValidator()

    def run_examples(self):
        """
        Ejecuta ejemplos que demuestran las capacidades de Pyre2.
        """
        print("Ejemplo 1: Validar correos electrónicos")
        email = "correo@example.com"
        is_valid = self.validator.validate_email(email)
        print(f"¿Es '{email}' un correo válido? {'Sí' if is_valid else 'No'}")

        print("\nEjemplo 2: Extraer fechas")
        text_with_dates = "Hoy es 2024-11-21, mañana será 2024-11-22."
        dates = self.validator.extract_dates(text_with_dates)
        print(f"Fechas encontradas: {dates}")

        print("\nEjemplo 3: Contar números en un texto")
        text_with_numbers = "Hay 3 gatos, 5 perros y 12 pájaros."
        number_count = self.validator.count_numbers(text_with_numbers)
        print(f"Números encontrados: {number_count}")

        print("\nEjemplo 4: Reemplazar palabras en un texto")
        handler = RegexHandler(r'\bperros\b')
        text = "Tengo perros y gatos."
        replaced_text = handler.replace(text, "aves")
        print(f"Texto original: {text}")
        print(f"Texto modificado: {replaced_text}")


# Ejecutar los ejemplos
if __name__ == "__main__":
    runner = Pyre2ExampleRunner()
    runner.run_examples()
