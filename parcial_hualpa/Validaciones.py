def validar_campos_no_vacios(*campos):
    """Valida que los campos no estén vacíos."""
    for campo in campos:
        if not campo or not campo.strip():
            return False
    return True

def validar_precio(precio_str):
    """Valida precio: numérico, flotante, > 0."""
    try:
        precio = float(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_stock(stock_str):
    """Valida stock: numérico, entero, >= 0."""
    try:
        stock = int(float(stock_str))
        return stock >= 0
    except ValueError:
        return False

def validar_nuevo_valor(campo, valor):
    """Valida nuevo valor según campo."""
    if campo == "precio":
        return validar_precio(valor)
    elif campo == "stock":
        return validar_stock(valor)
    elif campo in ["nombre", "descripcion"]:
        return validar_campos_no_vacios(valor)
    return True  # Para otros campos, asume válido