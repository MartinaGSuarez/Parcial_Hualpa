import csv
import os
import uuid
from estructura_inicial import asegurar_directorio_y_csv, construir_ruta, CSV_HEADERS
from lectura_rcursiva import recorrido_recursivo
from Validaciones import validar_campos_no_vacios, validar_precio, validar_stock, validar_nuevo_valor

def generar_id():
    return uuid.uuid4().hex

def alta_item(categoria, marca, linea, nombre, precio, stock, descripcion):
    """Crea las carpetas si no existen y agrega un nuevo producto."""
    if not validar_campos_no_vacios(categoria, marca, linea, nombre, descripcion):
        print("[Error] Todos los campos deben estar completos.")
        return
    if not validar_precio(precio) or not validar_stock(stock):
        print("[Error] Precio debe ser > 0 y stock >= 0.")
        return

    try:
        asegurar_directorio_y_csv(categoria, marca, linea)
        _, ruta_csv = construir_ruta(categoria, marca, linea)
        nuevo = {"id": generar_id(), "nombre": nombre, "precio": float(precio), "stock": int(float(stock)), "descripcion": descripcion}
        with open(ruta_csv, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writerow(nuevo)
        print("[OK] Producto agregado correctamente.")
    except (PermissionError, OSError) as e:
        print(f"[Error] No se pudo escribir el archivo: {e}")

def modificar_item(id_buscar, campo, nuevo_valor):
    """Modifica un campo de un producto existente."""
    if not validar_nuevo_valor(campo, nuevo_valor):
        print("[Error] Valor inválido para el campo.")
        return

    todos = recorrido_recursivo()
    for prod in todos:
        if prod["id"] == id_buscar:
            ruta = prod["ruta_archivo"]
            try:
                with open(ruta, "r", newline="", encoding="utf-8") as f:
                    datos = list(csv.DictReader(f))
                for fila in datos:
                    if fila["id"] == id_buscar:
                        fila[campo] = nuevo_valor
                with open(ruta, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
                    writer.writeheader()
                    writer.writerows(datos)
                print("[OK] Producto modificado.")
                return
            except (PermissionError, OSError) as e:
                print(f"[Error] No se pudo modificar: {e}")
                return
    print("[ERROR] No se encontró el ID especificado.")

def eliminar_item(id_buscar):
    """Elimina un producto por ID."""
    todos = recorrido_recursivo()
    for prod in todos:
        if prod["id"] == id_buscar:
            ruta = prod["ruta_archivo"]
            try:
                with open(ruta, "r", newline="", encoding="utf-8") as f:
                    datos = [x for x in csv.DictReader(f) if x["id"] != id_buscar]
                with open(ruta, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
                    writer.writeheader()
                    writer.writerows(datos)
                print("[OK] Producto eliminado.")
                return
            except (PermissionError, OSError) as e:
                print(f"[Error] No se pudo eliminar: {e}")
                return
    print("[ERROR] ID no encontrado.")