# Sistema de Gestión Jerárquica de Productos Tecnológicos

## Descripción
Este proyecto implementa un sistema de persistencia y consulta de datos para productos tecnológicos utilizando una estructura jerárquica de directorios en Python. La jerarquía es: **Categoría** (ej. Electrónica) -> **Marca** (ej. Samsung) -> **Línea** (ej. Smartphones). Los datos se almacenan en archivos CSV al final de cada rama jerárquica.

El sistema aplica recursividad para leer toda la estructura, y permite operaciones CRUD (Crear, Leer, Actualizar, Eliminar) con validaciones estrictas. Incluye filtrado, ordenamiento y estadísticas básicas.

## Estructura de Datos
- **Jerarquía:** Categoría -> Marca -> Línea
- **Atributos de Ítems:** id (único generado con UUID), nombre, precio (flotante > 0), stock (entero >= 0), descripción
- **Persistencia:** Archivos CSV con encabezados: ["id", "nombre", "precio", "stock", "descripcion"]
- **Lógica de Filtrado/Almacenamiento:** La jerarquía se mapea a carpetas (ej. `datos_productos/Electrónica/Samsung/Smartphones/productos.csv`). La recursividad lee todos los CSVs para consultas globales; el filtrado se hace en memoria por atributos jerárquicos o de ítem.

## Funcionalidades
- **Alta de Ítem:** Crea jerarquía de carpetas dinámicamente y agrega producto con validaciones (campos no vacíos, tipos numéricos, lógica de negocio).
- **Mostrar y Filtrar:** Lista todos los productos recursivamente con ubicación; filtra por categoría, marca, línea o nombre (búsqueda que contiene, case-insensitive).
- **Modificar Ítem:** Actualiza un campo específico de un producto identificado por ID, con validaciones.
- **Eliminar Ítem:** Borra un producto por ID y actualiza el CSV correspondiente.
- **Ordenar y Estadísticas:** Ordena por precio o nombre (ASC/DESC); muestra total de productos, suma y promedio de precios, y recuento por categoría de primer nivel.

## Instalación y Uso
1. Clona el repositorio: `git clone https://github.com/tuusuario/tu-repo.git`
2. Ejecuta el menú principal: `python Menu.py`
3. Sigue las opciones del menú para gestionar productos. La carpeta `datos_productos` se crea automáticamente.

## Requisitos
- Python 3.x
- Librerías estándar: `os`, `csv`, `uuid`, `collections`

## Estructura del Proyecto
- `Estructura_inicial.py`: Funciones para crear directorios, rutas seguras y asegurar CSVs.
- `Lectura_recursiva.py`: Función recursiva para recorrer jerarquía y leer CSVs.
- `validaciones.py`: Validaciones estrictas de datos (tipos, lógica, no vacíos).
- `Crud.py`: Operaciones CRUD con manejo de excepciones.
- `estadisticas_ordenamiento.py`: Funciones de ordenamiento y cálculo de estadísticas.
- `Menu.py`: Interfaz de usuario con menú interactivo.
- `README.md`: Esta documentación.

## Video Explicativo
[Enlace al video en YouTube o similar,https://youtu.be/tu-video ej. ] - El video explica el dominio elegido (productos tecnológicos), el diseño de la jerarquía, cómo se mapea a directorios, y demuestra la lógica de persistencia jerárquica (máximo 8 minutos).
