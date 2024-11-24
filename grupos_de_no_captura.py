import re

texto = "Juan compró 3 manzanas, María compró 5 peras, y Pedro compró 7 plátanos."

# Patrón usando grupos de no captura para las frutas
patron = r"(\w+) compró (\d+) (?:manzanas|peras|plátanos)"

# Buscar todas las coincidencias
coincidencias = re.findall(patron, texto)

# Mostrar las coincidencias
for nombre, cantidad in coincidencias:
    print(f"Nombre: {nombre}, Cantidad: {cantidad}")

