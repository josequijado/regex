import regex as re

class RegexAdvancedExamples:
    """
    Clase que muestra ejemplos avanzados del uso de la librería `regex` en Python.
    Cada método en esta clase ilustra una característica específica de `regex` como:
    - Coincidencias con límites.
    - Cuantificadores de retroceso y ancho variable.
    - Soporte avanzado para Unicode.
    - Coincidencias con solapamiento.

    Los métodos están diseñados para ser reutilizables, con un enfoque modular para analizar textos complejos.
    """

    def __init__(self, text):
        """
        Constructor de la clase.

        Inicializa la instancia con un texto base sobre el cual se aplicarán
        las expresiones regulares en los métodos.

        :param text: Cadena de texto donde se realizarán las búsquedas y operaciones.
        """
        self.text = text

    def boundary_matching(self, pattern):
        """
        Ilustra cómo funcionan las coincidencias con límites en `regex`.

        - Un límite de palabra (`\b`) coincide con una posición entre un carácter de palabra
          (letras o números) y un carácter no palabra (espacios, puntuación, etc.).
        - Esto es útil para buscar palabras completas en lugar de partes de palabras.

        :param pattern: Expresión regular que incluye límites de palabra para buscar coincidencias específicas.
        :return: Lista de coincidencias encontradas en el texto.
        """
        print(f"** Coincidencia de límites con el patrón '{pattern}' **")
        # Utilizamos re.findall para buscar todas las coincidencias en el texto.
        matches = re.findall(pattern, self.text)
        print(f"Coincidencias encontradas: {matches}")
        return matches

    def variable_width_quantifiers(self, pattern):
        """
        Ejemplo del uso de cuantificadores de ancho variable en `regex`.

        - Los cuantificadores "perezosos" (`*?`, `+?`, `{n,m}?`) intentan encontrar el menor número de coincidencias.
        - Esto contrasta con los cuantificadores "codiciosos" que buscan la mayor coincidencia posible.
        - Útil cuando necesitas controlar estrictamente el rango de coincidencias.

        :param pattern: Expresión regular con cuantificadores de ancho variable.
        :return: Lista de coincidencias encontradas en el texto.
        """
        print(f"\n** Cuantificadores de ancho variable con el patrón '{pattern}' **")
        # re.findall devuelve todas las coincidencias que cumplen con el patrón dado.
        matches = re.findall(pattern, self.text)
        print(f"Coincidencias encontradas: {matches}")
        return matches

    def unicode_support(self, pattern):
        """
        Muestra cómo manejar texto Unicode con la librería `regex`.

        - La clase `\p{L}` permite encontrar cualquier carácter que sea una letra,
          independientemente del alfabeto (por ejemplo, cirílico, árabe, chino, etc.).
        - Esto es muy útil para procesar textos multilingües o analizar datos de diferentes lenguajes.

        :param pattern: Expresión regular que utiliza clases Unicode para buscar caracteres específicos.
        :return: Lista de coincidencias encontradas en el texto.
        """
        print(f"\n** Soporte Unicode con el patrón '{pattern}' **")
        # Busca todas las secuencias de letras Unicode en el texto.
        matches = re.findall(pattern, self.text)
        print(f"Coincidencias encontradas: {matches}")
        return matches

    def overlapping_matches(self, pattern):
        """
        Ejemplo de coincidencias con solapamiento en `regex`.

        - Por defecto, las coincidencias no se solapan (una coincidencia bloquea las posteriores).
        - Usar el parámetro `overlapped=True` permite capturar coincidencias
          incluso si ya forman parte de una coincidencia anterior.
        - Útil para analizar repeticiones o patrones continuos.

        :param pattern: Expresión regular para buscar coincidencias con solapamiento.
        :return: Lista de coincidencias encontradas en el texto.
        """
        print(f"\n** Coincidencias con solapamiento con el patrón '{pattern}' **")
        # Habilita el solapamiento utilizando `overlapped=True`.
        matches = re.findall(pattern, self.text, overlapped=True)
        print(f"Coincidencias encontradas: {matches}")
        return matches


# Ejemplo de uso de la clase
if __name__ == "__main__":
    # Texto de ejemplo con diferentes patrones para ilustrar las características de `regex`.
    texto_ejemplo = (
        "El número 123 y 456 son ejemplos. "
        "También encontramos números como 789, 987 y 123456. "
        "A continuación, tenemos varias letras y símbolos."
    )

    # Crear instancia de la clase RegexAdvancedExamples.
    regex_example = RegexAdvancedExamples(texto_ejemplo)

    # 1. Coincidencia de límites
    # Buscar la palabra 'número' como una palabra completa.
    regex_example.boundary_matching(r"\bnúmero\b")

    # 2. Cuantificadores de retroceso y de ancho variable
    # Buscar números de 1 a 3 dígitos utilizando un cuantificador "perezoso".
    regex_example.variable_width_quantifiers(r"\d{1,3}?")

    # 3. Soporte para Unicode
    # Buscar todas las letras de cualquier idioma utilizando la clase `\p{L}`.
    regex_example.unicode_support(r"\p{L}+")

    # 4. Coincidencias con solapamiento
    # Buscar la letra 'a' y capturar coincidencias superpuestas.
    regex_example.overlapping_matches(r"a")
