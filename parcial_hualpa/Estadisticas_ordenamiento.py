from collections import Counter

def ordenar_productos(productos, criterio, ascendente=True):
    """Ordena la lista de productos por criterio (precio o nombre)."""
    if criterio == "precio":
        productos.sort(key=lambda x: float(x.get("precio", 0)), reverse=not ascendente)
    elif criterio == "nombre":
        productos.sort(key=lambda x: x.get("nombre", "").lower(), reverse=not ascendente)

def calcular_estadisticas(productos):
    """Calcula estadísticas: total, suma precios, promedio, recuento por Categoría."""
    total = len(productos)
    suma = sum(float(p.get("precio", 0)) for p in productos)
    prom = suma / total if total > 0 else 0
    categorias = Counter(p.get("categoria", "") for p in productos)
    return total, suma, prom, categorias