import re

class RegexExamples:
    """
    Clase que encapsula ejemplos de uso de la biblioteca `re` en Python.
    Esta clase ilustra las principales funcionalidades de `re` con métodos separados, 
    cada uno de los cuales muestra una funcionalidad específica de la librería.
    """

    def __init__(self, text):
        """
        Constructor de la clase que inicializa el texto sobre el cual se aplicarán las expresiones regulares.

        :param text: Cadena de texto donde se realizarán las búsquedas y operaciones.
        """
        self.text = text

    def search_pattern(self, pattern):
        """
        Busca la primera aparición de un patrón en el texto.

        :param pattern: Expresión regular a buscar en el texto.
        :return: Objeto Match si se encuentra el patrón, de lo contrario None.
        """
        match = re.search(pattern, self.text)
        if match:
            print(f"Encontrado: '{match.group()}' en la posición {match.start()} - {match.end()}")
        else:
            print("Patrón no encontrado.")
        return match

    def match_pattern(self, pattern):
        """
        Comprueba si el patrón coincide al inicio del texto.

        :param pattern: Expresión regular a verificar.
        :return: Objeto Match si el patrón coincide al inicio, None de lo contrario.
        """
        match = re.match(pattern, self.text)
        if match:
            print(f"Patrón '{match.group()}' encontrado al inicio de la cadena.")
        else:
            print("No hay coincidencia al inicio de la cadena.")
        return match

    def find_all_matches(self, pattern):
        """
        Encuentra todas las coincidencias del patrón en el texto.

        :param pattern: Expresión regular a buscar en el texto.
        :return: Lista con todas las coincidencias encontradas.
        """
        matches = re.findall(pattern, self.text)
        print(f"Coincidencias encontradas: {matches}")
        return matches

    def find_iter_matches(self, pattern):
        """
        Encuentra todas las coincidencias utilizando un iterador para obtener los detalles de posición.

        :param pattern: Expresión regular a buscar.
        :return: Lista de objetos Match detallando las coincidencias.
        """
        matches = list(re.finditer(pattern, self.text))
        for match in matches:
            print(f"Coincidencia: '{match.group()}' en posición {match.start()} - {match.end()}")
        return matches

    def replace_pattern(self, pattern, replacement):
        """
        Reemplaza todas las coincidencias del patrón en el texto con un nuevo valor.

        :param pattern: Expresión regular de las coincidencias a reemplazar.
        :param replacement: Texto con el que se reemplazarán las coincidencias.
        :return: Cadena de texto con las coincidencias reemplazadas.
        """
        new_text = re.sub(pattern, replacement, self.text)
        print(f"Texto después de reemplazar: {new_text}")
        return new_text

    def split_text(self, pattern):
        """
        Divide el texto en una lista de subcadenas utilizando el patrón como delimitador.

        :param pattern: Expresión regular usada para dividir el texto.
        :return: Lista de subcadenas resultantes.
        """
        parts = re.split(pattern, self.text)
        print(f"Texto dividido: {parts}")
        return parts

    def substitute_with_count(self, pattern, replacement):
        """
        Reemplaza coincidencias y devuelve el texto resultante y el número de reemplazos.

        :param pattern: Expresión regular para las coincidencias a reemplazar.
        :param replacement: Texto con el que se reemplazarán las coincidencias.
        :return: Tupla que contiene el texto con reemplazos y el número de reemplazos.
        """
        new_text, num_replacements = re.subn(pattern, replacement, self.text)
        print(f"Texto tras reemplazos: {new_text}, número de reemplazos: {num_replacements}")
        return new_text, num_replacements

    def extract_groups(self, pattern):
        """
        Extrae grupos de una coincidencia de patrón con paréntesis.

        :param pattern: Expresión regular con grupos para extraer.
        :return: Lista de tuplas con los grupos extraídos.
        """
        matches = re.finditer(pattern, self.text)
        groups = [match.groups() for match in matches]
        print(f"Grupos extraídos: {groups}")
        return groups

# Ejemplo de uso
if __name__ == "__main__":
    texto_ejemplo = "El número de teléfono es +34 123 456 789 y el correo es ejemplo@correo.com."

    regex_example = RegexExamples(texto_ejemplo)

    # Ejemplos de uso de cada método
    regex_example.search_pattern(r"\d{3}")            # Busca la primera secuencia de 3 dígitos
    regex_example.match_pattern(r"El número")         # Verifica si empieza con "El número"
    regex_example.find_all_matches(r"\d{3}")          # Encuentra todas las secuencias de 3 dígitos
    regex_example.find_iter_matches(r"\d{3}")         # Encuentra todas las secuencias de 3 dígitos con detalles de posición
    regex_example.replace_pattern(r"\d{3}", "***")    # Reemplaza secuencias de 3 dígitos con "***"
    regex_example.split_text(r"\s")                   # Divide el texto en palabras usando espacios como delimitadores
    regex_example.substitute_with_count(r"\d{3}", "###")  # Reemplaza secuencias de 3 dígitos y cuenta los reemplazos
    regex_example.extract_groups(r"(\+\d{2}) (\d{3}) (\d{3}) (\d{3})")  # Extrae grupos del número de teléfono
