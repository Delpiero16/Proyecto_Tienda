import os

# ==========================
# ARCHIVO
# Variable donde se guarda el nombre del archivo de texto.
# En este archivo se almacenan los productos para no perderlos al cerrar el programa.
# ==========================

ARCHIVO = "inventario.txt"

# ==========================
# LISTAS
# listas paralelas del inventario.
# cada posicion representa un mismo producto.
# ejemplo: categorias[0] nombres_productos[0] y asi los demas 
# pertenecen al mismo producto.
# ==========================

categorias = []
nombres_productos = []
stock_productos = []
precios_productos = []

# lista donde se guardan las ventas realizadas durante el programa.
historial_ventas = []
historial_cantidades = []
historial_totales = []

# Constante que indica el limite del sistema 
MAX_PRODUCTOS = 50
MAX_STOCK = 36

# ==========================
# CARGAR ARCHIVO
# Sirve para leer los productos guardados en el invetario.txt
# Se ejecuta al iniciar el programa para recuperar la informacion anterior.
# Si el archivo no existe, no carga nada y el programa empieza vacio.
# ==========================

def cargar_archivo():

    if not os.path.exists(ARCHIVO):
        return

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:

        for linea in archivo: 

            datos = linea.strip().split(",")

            if len(datos) == 3:

                categorias.append(datos[0])
                nombres_productos.append(datos[1])
                stock_productos.append(int(datos[2]))
                precios_productos.append(0)

            elif len(datos) == 4:

                categorias.append(datos[0])
                nombres_productos.append(datos[1])
                stock_productos.append(int(datos[2]))
                precios_productos.append(float(datos[3]))

# ==========================
# GUARDAR ARCHIVO
# Sirve para guardar todos los productos del inventario en el archivo inventario.txt
# Se usa despues de agregar, eliminar productos o registrar ventas. 
# ==========================

def guardar_archivo():

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:

        for i in range(len(nombres_productos)):

            archivo.write(
                categorias[i] + "," +
                nombres_productos[i] + "," +
                str(stock_productos[i]) + "," +
                str(precios_productos[i]) + "\n"
            )

# ==========================
# CREATE (agregar_producto)
# Cumple la funcion del CRUD
# permite registrar un nuevo producto con categoria, nombre, precio y cantidad.
# Tambien verifica que no se supere el maximo de productos ni el stock maximo.
# ==========================

def agregar_producto():

    print("\n--- AGREGAR PRODUCTO ---")

    if len(nombres_productos) >= MAX_PRODUCTOS:
        print("Error: Se alcanzó el límite de productos.")
        return

    print("\nCategorias")
    print("1. Bebidas")
    print("2. Fideos")
    print("3. Lacteos")
    print("4. Snacks")
    print("5. Limpieza")

    opcion = input("Seleccione categoria: ")

    categoria = ""

    if opcion == "1":
        categoria = "Bebidas"

    elif opcion == "2":
        categoria = "Fideos"

    elif opcion == "3":
        categoria = "Lacteos"

    elif opcion == "4":
        categoria = "Snacks"

    elif opcion == "5":
        categoria = "Limpieza"

    else:
        print("Categoria incorrecta")
        return
    
    nombre = input("Nombre del producto: ").strip().title()
    
    precio_texto = input("Precio del producto: ")

    while not precio_texto.replace(".", "", 1).isdigit():

        print("Ingrese un precio valido")

        precio_texto = input("Precio del producto: ")

    precio = float(precio_texto)

    while nombre == "":
        print("Nombre inválido")
        nombre = input("Nombre del producto: ").strip().title()

    cantidad_texto = input("Cantidad: ")

    while not cantidad_texto.isdigit():
        print("Ingrese solo numeros")
        cantidad_texto = input("Cantidad: ")

    cantidad = int(cantidad_texto)

    if cantidad > MAX_STOCK:
        print("Error: Maximo stock permitido =", MAX_STOCK)
        return

    encontrado = False

    for i in range(len(nombres_productos)):

        if nombres_productos[i] == nombre:

            if stock_productos[i] >= MAX_STOCK:
                print("⚠ SE HA LLEGADO AL LIMITE DEL STOCK (36)")
                print("No se puede agregar más cantidad.")
                return

            if stock_productos[i] + cantidad > MAX_STOCK:
                print("⚠ ERROR: NO SE PUEDE SUPERAR EL STOCK MAXIMO DE 36")
                print("Stock actual:", stock_productos[i])
                return

            stock_productos[i] += cantidad
            precios_productos[i] = precio

            encontrado = True

            guardar_archivo()

            print("Stock actualizado")
            print("Nuevo stock:", stock_productos[i])

            if stock_productos[i] == MAX_STOCK:
                print("⚠ SE HA LLEGADO AL LIMITE DEL STOCK (36)")

    if encontrado == False:

        categorias.append(categoria)
        nombres_productos.append(nombre)
        stock_productos.append(cantidad)
        precios_productos.append(precio)

        guardar_archivo()

        print("Producto agregado correctamente")

        if cantidad == MAX_STOCK:
            print("⚠ SE HA LLEGADO AL LIMITE DEL STOCK (36)")

# ==========================
# READ (mostar_producto)
# Cumple la funcion CRUD
# Muestra en pantalla todos los productos guardados en el inventario.
# Presenta categoria, nombre, precio y stock de cada producto.
# ==========================

def mostrar_productos():

    print("\n--- INVENTARIO ---")

    if len(nombres_productos) == 0:
        print("No existen productos")
        return

    for i in range(len(nombres_productos)):

       print(
           "Categoria:", categorias[i],
           "| Producto:", nombres_productos[i],
           "| Precio:", round(precios_productos[i], 2),
           "| Stock:", stock_productos[i]
        )

# ==========================
# RESUMEN DEL INVENTARIO
# Sirve para mostrar un resumen general del inventario.
# Indica cuantos productos hay registrados y suma todo el stock alamcenado.
# ==========================

def resumen_inventario():

    print("\n--- RESUMEN DEL INVENTARIO ---")

    print("Cantidad de productos:", len(nombres_productos))

    total_stock = 0

    for i in range(len(stock_productos)):

        total_stock = total_stock + stock_productos[i]

    print("Total de unidades almacenadas:", total_stock)

# ==========================
# BUSCAR 
# Sirve para buscar un producto por su nombre.
# Compara el nombre registrado con los productos registrados.
# si lo encuentra, muestra su categoria, precio y stock.
# ==========================

def buscar_producto():

    print("\n--- BUSCAR PRODUCTO ---")

    nombre = input("Ingrese producto: ").strip().lower()

    encontrado = False

    for i in range(len(nombres_productos)):

        if nombres_productos[i].strip().lower() == nombre:

            print("\nProducto encontrado")
            print("Categoria:", categorias[i])
            print("Producto:", nombres_productos[i])
            print("Precio:", precios_productos[i])
            print("Stock:", stock_productos[i])

            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado")

# ==========================
# UPDATE
# ==========================

def actualizar_producto():

    nombre = input("Producto a actualizar: ").strip().lower()

    encontrado = False

    for i in range(len(nombres_productos)):

        if nombres_productos[i].strip().lower() == nombre:

            cantidad_texto = input("Nuevo stock: ")

            while not cantidad_texto.isdigit():
                print("Ingrese solo numeros")
                cantidad_texto = input("Nuevo stock: ")

            nuevo_stock = int(cantidad_texto)

            if nuevo_stock > MAX_STOCK:
               print("⚠ ERROR: EL STOCK MAXIMO PERMITIDO ES 36")
               return

            if nuevo_stock == MAX_STOCK:
               print("⚠ SE HA LLEGADO AL LIMITE DEL STOCK (36)")

            stock_productos[i] = nuevo_stock

            guardar_archivo()

            print("Producto actualizado")

            encontrado = True

    if encontrado == False:
        print("Producto no encontrado")
# ==========================
# DELETE
# ==========================

def eliminar_producto():

    nombre = input("Producto a eliminar: ").strip().lower()

    encontrado = False

    for i in range(len(nombres_productos)):

        if nombres_productos[i].strip().lower() == nombre:

            categorias.pop(i)
            nombres_productos.pop(i)
            stock_productos.pop(i)
            precios_productos.pop(i)

            guardar_archivo()

            print("Producto eliminado")

            encontrado = True

            break

    if encontrado == False:
        print("Producto no encontrado")

