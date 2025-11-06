import sys
from crud import alta_item, modificar_item, eliminar_item
from lectura_rcursiva import recorrido_recursivo
from estructura_inicial import asegurar_raiz
from Estadisticas_ordenamiento import ordenar_productos, calcular_estadisticas

def mostrar_item(prod):
    print(f"""
ID: {prod.get('id')}
Nombre: {prod.get('nombre')}
Precio: {prod.get('precio')}
Stock: {prod.get('stock')}
Descripcion: {prod.get('descripcion')}
Ubicacion: {prod.get('categoria')} / {prod.get('marca')} / {prod.get('linea')}
""")

def menu():
    asegurar_raiz()
    while True:
        print("""
---------- MENÚ -----------
1. Alta de producto
2. Mostrar y filtrar productos
3. Modificar producto
4. Eliminar producto
5. Ordenar / Estadísticas
0. Salir
-------------------------
""")
        op = input("Opción: ")
        if op == "1":
            categoria = input("Categoría: ")
            marca = input("Marca: ")
            linea = input("Línea: ")
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            stock = input("Stock: ")
            descripcion = input("Descripción: ")
            alta_item(categoria, marca, linea, nombre, precio, stock, descripcion)

        elif op == "2":
            productos = recorrido_recursivo()
            if not productos:
                print("[INFO] No hay productos.")
                continue
            for p in productos:
                mostrar_item(p)
            if input("¿Filtrar lista? (s/n): ").lower() == "s":
                campo = input("Filtrar por (categoria/marca/linea/nombre): ")
                valor = input("Valor (contiene): ").lower()
                filtrados = [x for x in productos if valor in x.get(campo, "").lower()]
                for p in filtrados:
                    mostrar_item(p)

        elif op == "3":
            id_mod = input("ID del producto a modificar: ")
            campo = input("Campo a modificar (nombre/precio/stock/descripcion): ")
            nuevo = input("Nuevo valor: ")
            modificar_item(id_mod, campo, nuevo)

        elif op == "4":
            id_del = input("ID del producto a eliminar: ")
            eliminar_item(id_del)

        elif op == "5":
            productos = recorrido_recursivo()
            if not productos:
                print("[INFO] No hay productos.")
                continue
            print("1. Ordenar por precio ASC\n2. Ordenar por precio DESC\n3. Ordenar por nombre ASC\n4. Ordenar por nombre DESC\n5. Estadísticas")
            sub = input("Opción: ")
            if sub in ["1", "2", "3", "4"]:
                criterio = "precio" if sub in ["1", "2"] else "nombre"
                asc = sub in ["1", "3"]
                ordenar_productos(productos, criterio, asc)
                for p in productos:
                    mostrar_item(p)
            elif sub == "5":
                total, suma, prom, categorias = calcular_estadisticas(productos)
                print(f"Total productos: {total}\nSuma precios: {suma:.2f}\nPromedio precio: {prom:.2f}")
                print("Recuento por Categoría:")
                for cat, count in categorias.items():
                    print(f"  {cat}: {count}")

        elif op == "0":
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()