import re

class DocumentoIdentidadValidator:
    """
    Clase para validar documentos de identidad españoles: NIF y NIE.
    Identifica automáticamente el tipo de documento y verifica su formato y letra.
    """
    
    # Tabla de letras válidas para los restos del módulo 23
    LETRAS_NIF = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    def __init__(self):
        # Patrones para NIF y NIE
        self.pattern_nif = re.compile(r'^\d{8}[A-Z]$')  # Ocho dígitos y una letra
        self.pattern_nie = re.compile(r'^[XYZ]\d{7}[A-Z]$')  # X, Y o Z seguido de siete dígitos y una letra

    def identificar_documento(self, doc: str) -> str:
        """
        Identifica el tipo de documento: NIF o NIE.
        
        Args:
            doc (str): Documento a identificar.
        
        Returns:
            str: 'NIF', 'NIE' si se identifica correctamente, o 'Desconocido'.
        """
        if self.pattern_nif.match(doc):
            return 'NIF'
        elif self.pattern_nie.match(doc):
            return 'NIE'
        return 'Desconocido'

    def validar_formato(self, doc: str) -> bool:
        """
        Valida si el documento tiene un formato correcto (NIF o NIE).
        
        Args:
            doc (str): Documento a validar.
        
        Returns:
            bool: True si el formato es válido, False en caso contrario.
        """
        return bool(self.pattern_nif.match(doc) or self.pattern_nie.match(doc))

    def calcular_letra_nif(self, numero: int) -> str:
        """
        Calcula la letra correcta de un NIF a partir de su número.
        
        Args:
            numero (int): Número del NIF.
        
        Returns:
            str: Letra correspondiente.
        """
        return self.LETRAS_NIF[numero % 23]

    def validar_letra(self, doc: str) -> bool:
        """
        Valida si la letra del documento es correcta.
        
        Args:
            doc (str): Documento a validar.
        
        Returns:
            bool: True si la letra es correcta, False en caso contrario.
        """
        tipo = self.identificar_documento(doc)
        if tipo == 'NIF':
            numero = int(doc[:-1])  # Ocho dígitos del NIF
            letra_correcta = self.calcular_letra_nif(numero)
        elif tipo == 'NIE':
            # Sustituimos la letra inicial por su número correspondiente
            conversion = {'X': '0', 'Y': '1', 'Z': '2'}
            numero = int(conversion[doc[0]] + doc[1:-1])  # Convertimos el NIE a un número
            letra_correcta = self.calcular_letra_nif(numero)
        else:
            return False  # Tipo desconocido

        return doc[-1] == letra_correcta

    def validar_documento(self, doc: str) -> str:
        """
        Valida un documento completamente (formato y letra).
        
        Args:
            doc (str): Documento a validar.
        
        Returns:
            str: Mensaje indicando si es válido y el tipo de documento.
        """
        tipo = self.identificar_documento(doc)
        if tipo == 'Desconocido':
            return f"El documento '{doc}' tiene un formato inválido."

        if self.validar_formato(doc) and self.validar_letra(doc):
            return f"El documento '{doc}' es un {tipo} válido."
        else:
            return f"El documento '{doc}' es un {tipo} inválido."


# Ejemplo de uso
if __name__ == "__main__":
    validator = DocumentoIdentidadValidator()

    # Pruebas de NIF y NIE
    documentos = ["12345678Z", "X1234567L", "Y1234567X", "Z7654321M", "12345678A", "X1234567A"]

    for doc in documentos:
        print(validator.validar_documento(doc))
