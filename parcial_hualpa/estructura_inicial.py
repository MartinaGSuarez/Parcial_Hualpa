import os
import csv

# Carpeta raíz donde se almacenarán todos los datos
ROOT_DIR = os.path.join(os.getcwd(), "datos_productos")
CSV_FILENAME = "productos.csv"
CSV_HEADERS = ["id", "nombre", "precio", "stock", "descripcion"]

def asegurar_raiz():
    """Crea la carpeta raíz si no existe."""
    os.makedirs(ROOT_DIR, exist_ok=True)

def safe_filename(nombre: str) -> str:
    """Convierte un texto en nombre seguro de carpeta."""
    return "".join(c for c in nombre.strip() if c.isalnum() or c in (" ", "_", "-")).rstrip()

def construir_ruta(categoria, marca, linea):
    """Devuelve la ruta completa del CSV para esa jerarquía."""
    ruta_dir = os.path.join(ROOT_DIR, safe_filename(categoria), safe_filename(marca), safe_filename(linea))
    ruta_csv = os.path.join(ruta_dir, CSV_FILENAME)
    return ruta_dir, ruta_csv

def asegurar_directorio_y_csv(categoria, marca, linea):
    """Crea carpetas y CSV con encabezado si no existen."""
    ruta_dir, ruta_csv = construir_ruta(categoria, marca, linea)
    os.makedirs(ruta_dir, exist_ok=True)
    if not os.path.exists(ruta_csv):
        with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()