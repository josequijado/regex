import re

texto = "Hola, mi nombre es Juan y mi número es 12345."
patron = r"mi nombre es (\w+) y mi número es (\d+)"
coincidencia = re.search(patron, texto)

if coincidencia:
    nombre = coincidencia.group(1)  # Primer grupo capturado: "Juan"
    numero = coincidencia.group(2)  # Segundo grupo capturado: "12345"
    print(f"Nombre: {nombre}, Número: {numero}")

