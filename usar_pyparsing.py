# Importaciones de PyParsing, cada una explicada:
from pyparsing import (
    Word,         # Permite definir gramáticas que coincidan con palabras compuestas por ciertos caracteres (e.g., letras, números).
    alphas,       # Conjunto predefinido que incluye todas las letras del alfabeto (a-z, A-Z).
    nums,         # Conjunto predefinido que incluye todos los dígitos (0-9).
    alphanums,    # Conjunto predefinido que incluye letras (a-z, A-Z) y dígitos (0-9).
    Literal,      # Representa una coincidencia exacta con un texto literal (e.g., "+" para un operador).
    OneOrMore,    # Indica que un elemento debe aparecer al menos una vez en la gramática.
    Group,        # Agrupa elementos de una gramática para tratarlos como una sola unidad.
    Optional,     # Indica que un elemento es opcional dentro de la gramática.
    delimitedList, # Permite definir listas separadas por un delimitador, como comas.
    infixNotation, # Facilita la definición de expresiones matemáticas con operadores y prioridades.
    opAssoc,      # Especifica la asociatividad de operadores (izquierda o derecha).
    Suppress,     # Oculta un elemento del resultado final, aunque sea parte de la gramática.
)

class PyParsingTutorial:
    """
    Clase que ilustra el uso de PyParsing para diversos tipos de análisis y procesamiento de texto.
    Esta clase está diseñada para ser extremadamente didáctica, con múltiples ejemplos que cubren
    distintos escenarios de uso, desde análisis simples hasta estructuras complejas.
    """

    def __init__(self):
        """
        Constructor de la clase. Inicializa cualquier dato necesario para las operaciones.
        En este caso, no se requieren variables globales persistentes para los métodos.
        """
        pass

    def parse_simple_sentence(self, text):
        """
        Ejemplo básico: Analiza una oración en formato sujeto-verbo-objeto directo.

        **Propósito:**
        Este ejemplo demuestra cómo analizar texto siguiendo una gramática muy simple.

        **Gramática:**
        - Sujeto: Una palabra que empieza con mayúscula y puede tener minúsculas.
        - Verbo: Una palabra en minúsculas.
        - Objeto: Una palabra en minúsculas.

        :param text: Cadena que representa una oración simple (e.g., "Juan corre rápido").
        :return: Estructura jerárquica del análisis o un mensaje de error.
        """
        # Definimos las reglas de la gramática
        subject = Word(alphas.upper(), alphas.lower())("subject")  # Sujeto
        verb = Word(alphas.lower())("verb")  # Verbo
        obj = Word(alphas.lower())("object")  # Objeto

        # Combinamos las reglas en una oración
        sentence = subject + verb + obj

        # Intentamos analizar la oración
        try:
            result = sentence.parseString(text, parseAll=True)
            print(f"Análisis completado para '{text}': {result.dump()}")
            return result.asDict()
        except Exception as e:
            print(f"Error al analizar la oración '{text}': {e}")
            return None

    def parse_comma_separated_values(self, text):
        """
        Ejemplo: Analiza una lista de valores separados por comas.

        **Propósito:**
        Este ejemplo muestra cómo manejar datos tabulares o listas de valores.

        **Gramática:**
        - Una lista de números o palabras separados por comas.

        :param text: Cadena que representa una lista de valores separados por comas (e.g., "1, 2, 3").
        :return: Lista de valores analizados o un mensaje de error.
        """
        # Definimos la regla para un número o palabra
        value = Word(alphanums)
        # Definimos una lista de valores separados por comas
        value_list = delimitedList(value)("values")

        # Intentamos analizar la lista
        try:
            result = value_list.parseString(text, parseAll=True)
            print(f"Análisis completado para '{text}': {result.dump()}")
            return result.asList()
        except Exception as e:
            print(f"Error al analizar los valores separados por comas '{text}': {e}")
            return None

    def parse_math_expression(self, text):
        """
        Ejemplo: Analiza una expresión matemática con operadores y prioridad jerárquica.

        **Propósito:**
        Este ejemplo demuestra cómo analizar y organizar expresiones matemáticas.

        **Gramática:**
        - Operandos: Números enteros.
        - Operadores: +, -, *, /.
        - Prioridad: Multiplicación y división tienen mayor precedencia que suma y resta.

        :param text: Cadena que representa una expresión matemática (e.g., "3 + 5 * 2").
        :return: Estructura jerárquica del análisis o un mensaje de error.
        """
        # Componentes básicos
        number = Word(nums)("operand")  # Un número entero
        plus = Literal("+")  # Suma
        minus = Literal("-")  # Resta
        multiply = Literal("*")  # Multiplicación
        divide = Literal("/")  # División

        # Gramática jerárquica usando notación infija
        expression = infixNotation(
            number,
            [
                (multiply | divide, 2, opAssoc.LEFT),  # Multiplicación y división
                (plus | minus, 2, opAssoc.LEFT),  # Suma y resta
            ],
        )

        # Intentamos analizar la expresión matemática
        try:
            result = expression.parseString(text, parseAll=True)
            print(f"Análisis completado para '{text}': {result.dump()}")
            return result.asList()
        except Exception as e:
            print(f"Error al analizar la expresión matemática '{text}': {e}")
            return None

    def parse_key_value_pairs(self, text):
        """
        Ejemplo: Analiza pares clave-valor en formato estilo JSON simplificado.

        **Propósito:**
        Este ejemplo muestra cómo analizar estructuras jerárquicas simples como configuraciones o datos.

        **Gramática:**
        - Un par clave-valor separado por ":".
        - Se pueden incluir múltiples pares separados por espacios.

        :param text: Cadena que representa pares clave-valor (e.g., "nombre:Juan edad:30").
        :return: Lista de pares clave-valor o un mensaje de error.
        """
        # Componentes básicos: clave y valor
        key = Word(alphas)("key")  # Clave
        value = Word(alphas + nums)("value")  # Valor
        # Pares clave-valor
        pair = Group(key + Suppress(":") + value)("pair")
        # Lista de pares
        pairs = OneOrMore(pair)("pairs")

        # Intentamos analizar los pares clave-valor
        try:
            result = pairs.parseString(text, parseAll=True)
            print(f"Análisis completado para '{text}': {result.dump()}")
            return result.asList()
        except Exception as e:
            print(f"Error al analizar los pares clave-valor '{text}': {e}")
            return None

    def main(self):
        """
        Método principal que coordina la ejecución de los métodos anteriores.
        Cada método se ejecuta con ejemplos específicos para demostrar sus capacidades.
        """
        print("=== Ejemplo 1: Análisis de una oración simple ===")
        self.parse_simple_sentence("Juan corre rápido")

        print("\n=== Ejemplo 2: Lista de valores separados por comas ===")
        self.parse_comma_separated_values("apple, banana, cherry")

        print("\n=== Ejemplo 3: Expresión matemática ===")
        self.parse_math_expression("3 + 5 * 2 - 8 / 4")

        print("\n=== Ejemplo 4: Pares clave-valor ===")
        self.parse_key_value_pairs("nombre:Juan edad:30 profesion:Ingeniero")


# Punto de entrada principal
if __name__ == "__main__":
    tutorial = PyParsingTutorial()
    tutorial.main()
