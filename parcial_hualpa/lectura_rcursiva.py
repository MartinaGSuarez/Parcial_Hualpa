import os
import csv
from estructura_inicial import ROOT_DIR, CSV_FILENAME

def leer_csv(ruta_csv):
    """Lee un CSV y lo devuelve como lista de diccionarios."""
    datos = []
    try:
        with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                fila["precio"] = float(fila.get("precio", 0) or 0)
                fila["stock"] = int(float(fila.get("stock", 0) or 0))
                datos.append(fila)
    except (FileNotFoundError, ValueError, PermissionError):
        pass  # Ignora errores de lectura
    return datos

def recorrido_recursivo(ruta=None):
    """
    Recorre recursivamente toda la jerarquía de carpetas.
    Devuelve una lista de diccionarios con los productos y su ubicación.
    """
    if ruta is None:
        ruta = ROOT_DIR

    items = []
    try:
        for entrada in os.listdir(ruta):
            ruta_completa = os.path.join(ruta, entrada)
            if os.path.isdir(ruta_completa):
                items.extend(recorrido_recursivo(ruta_completa))
            elif entrada == CSV_FILENAME:
                partes = ruta_completa.split(os.sep)
                categoria = partes[-4] if len(partes) > 3 else ""
                marca = partes[-3] if len(partes) > 2 else ""
                linea = partes[-2] if len(partes) > 1 else ""
                registros = leer_csv(ruta_completa)
                for reg in registros:
                    reg["categoria"] = categoria
                    reg["marca"] = marca
                    reg["linea"] = linea
                    reg["ruta_archivo"] = ruta_completa
                    items.append(reg)
    except (FileNotFoundError, PermissionError, OSError):
        return []  # Maneja errores de acceso
    return items