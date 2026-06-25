import os

# ==========================
# ARCHIVO
# ==========================

ARCHIVO = "inventario.txt"

# ==========================
# LISTAS
# ==========================

categorias = []
nombres_productos = []
stock_productos = []
precios_productos = []

historial_ventas = []
historial_cantidades = []
historial_totales = []

MAX_PRODUCTOS = 50
MAX_STOCK = 36

# ==========================
# CARGAR ARCHIVO
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

def mostrar_tabla_productos():

    print("\n================== INVENTARIO ==================")
    print("N°  PRODUCTO               PRECIO      STOCK")
    print("------------------------------------------------")

    for i in range(len(nombres_productos)):

        print(
            f"{i + 1:<3} {nombres_productos[i]:<22} "
            f"S/. {precios_productos[i]:<8.2f} "
            f"{stock_productos[i]}"
        )

    print("------------------------------------------------")

# ==========================
# CREATE
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
# READ
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
# ==========================

def buscar_producto():

    print("\n--- BUSCAR PRODUCTO ---")

    if len(nombres_productos) == 0:
        print("No existen productos registrados.")
        return

    mostrar_tabla_productos()

    opcion = input("Seleccione el número del producto: ")

    while not opcion.isdigit():
        print("Ingrese solo números.")
        opcion = input("Seleccione el número del producto: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > len(nombres_productos):
        print("Número incorrecto.")
        return

    indice = opcion - 1

    print("\nProducto encontrado")
    print("Categoria:", categorias[indice])
    print("Producto:", nombres_productos[indice])
    print("Precio:", precios_productos[indice])
    print("Stock:", stock_productos[indice])

# ==========================
# UPDATE
# ==========================

def actualizar_producto():

    print("\n--- ACTUALIZAR PRODUCTO ---")

    if len(nombres_productos) == 0:
        print("No existen productos registrados.")
        return

    mostrar_tabla_productos()

    opcion = input("Seleccione el número del producto: ")

    while not opcion.isdigit():
        print("Ingrese solo números.")
        opcion = input("Seleccione el número del producto: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > len(nombres_productos):
        print("Número incorrecto.")
        return

    indice = opcion - 1

    cantidad_texto = input("Nuevo stock: ")

    while not cantidad_texto.isdigit():
        print("Ingrese solo números.")
        cantidad_texto = input("Nuevo stock: ")

    nuevo_stock = int(cantidad_texto)

    if nuevo_stock > MAX_STOCK:
        print("⚠ ERROR: EL STOCK MÁXIMO ES 36")
        return

    if nuevo_stock == MAX_STOCK:
        print("⚠ SE HA LLEGADO AL LÍMITE DEL STOCK (36)")

    stock_productos[indice] = nuevo_stock

    guardar_archivo()

    print("\nProducto actualizado correctamente.")
    print("Producto:", nombres_productos[indice])
    print("Nuevo stock:", stock_productos[indice])

# ==========================
# DELETE
# ==========================

def eliminar_producto():

     print("\n--- ELIMINAR PRODUCTO ---")

     if len(nombres_productos) == 0:
        print("No existen productos registrados.")
        return

     mostrar_tabla_productos()

     opcion = input("Seleccione el número del producto: ")

     while not opcion.isdigit():
        print("Ingrese solo números.")
        opcion = input("Seleccione el número del producto: ")

     opcion = int(opcion)

     if opcion < 1 or opcion > len(nombres_productos):
        print("Número incorrecto.")
        return

     indice = opcion - 1

     print("Producto eliminado:", nombres_productos[indice])

     categorias.pop(indice)
     nombres_productos.pop(indice)
     stock_productos.pop(indice)
     precios_productos.pop(indice)

     guardar_archivo()

# ==========================
# REGISTRAR VENTA
# ==========================

def registrar_venta():

    print("\n--- REGISTRAR VENTA ---")

    if len(nombres_productos) == 0:
        print("No existen productos registrados.")
        return

    mostrar_tabla_productos()

    opcion = input("Seleccione el número del producto: ")

    while not opcion.isdigit():
        print("Ingrese solo números.")
        opcion = input("Seleccione el número del producto: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > len(nombres_productos):
        print("Número incorrecto.")
        return

    indice = opcion - 1

    cantidad_texto = input("Cantidad vendida: ")

    while not cantidad_texto.isdigit():
        print("Ingrese solo números.")
        cantidad_texto = input("Cantidad vendida: ")

    cantidad = int(cantidad_texto)

    if cantidad > stock_productos[indice]:
        print("No hay suficiente stock.")
        return

    stock_productos[indice] -= cantidad

    total = cantidad * precios_productos[indice]

    historial_ventas.append(nombres_productos[indice])
    historial_cantidades.append(cantidad)
    historial_totales.append(total)

    guardar_archivo()

    print("\nVENTA REGISTRADA")
    print("Producto:", nombres_productos[indice])
    print("Cantidad:", cantidad)
    print("Total vendido: S/.", total)
    print("Stock restante:", stock_productos[indice])

    if stock_productos[indice] <= 5:
        print("⚠ ALERTA: STOCK BAJO")
        
# ==========================
# HISTORIAL DE VENTAS
# ==========================

def mostrar_historial():

    print("\n--- HISTORIAL DE VENTAS ---")

    if len(historial_ventas) == 0:

        print("No existen ventas")
        return

    for i in range(len(historial_ventas)):

        print(
            "Producto:", historial_ventas[i],
            "| Cantidad:", historial_cantidades[i],
            "| Total:", historial_totales[i]
        )
        
# ==========================
# REPORTE DE VENTAS
# ==========================

def reporte_ventas():

    print("\n--- REPORTE DE VENTAS ---")

    total_general = 0

    for i in range(len(historial_totales)):

        total_general = total_general + historial_totales[i]

    print("Total vendido:", total_general)

# ==========================
# REPORTE STOCK BAJO
# ==========================

def reporte_stock_bajo():

    print("\n--- PRODUCTOS CON STOCK BAJO ---")

    encontrado = False

    for i in range(len(nombres_productos)):

        if stock_productos[i] <= 5:

            print(
                "Producto:", nombres_productos[i],
                "| Stock:", stock_productos[i]
            )

            encontrado = True

    if encontrado == False:

        print("No existen productos con stock bajo")

# ==========================
# MENU
# ==========================

def menu():

    opcion = "0"

    while opcion != "11":

        print("\n===== SISTEMA DE INVENTARIO =====")
        print("Productos:", len(nombres_productos), "/", MAX_PRODUCTOS)
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Registrar venta")
        print("7. Historial de ventas")
        print("8. Reporte stock bajo")
        print("9. Resumen inventario")
        print("10. Reporte de ventas")
        print("11. Salir")
        opcion = input("Seleccione opcion: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            actualizar_producto()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            registrar_venta()

        elif opcion == "7":
            mostrar_historial()

        elif opcion == "8":
            reporte_stock_bajo()

        elif opcion == "9":
            resumen_inventario()

        elif opcion == "10":
            reporte_ventas()

        elif opcion == "11":
            print("Programa finalizado")
        
        else:
            print("Opcion incorrecta")

# ==========================
# INICIO DEL PROGRAMA
# ==========================

cargar_archivo()
menu()