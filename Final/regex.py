from re import match

def validar(valor):
    """
    Esta funcion recibe el valor ingresado en un campo y lo matchea con una Regex.

    Args:
        :valor(String): Contenido del campo a analizar.

    :returns: Boolean.
    
    """
    patron = "^[0-9]+$"
    if match(patron, valor):
        return True
    else:
        return False
    

# Nicolás Campanella Lerra
# Curso 999188622
# Python 3 - Nivel Intermedio