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

historial_ventas = []
historial_cantidades = []
historial_totales = []

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

def mostrar_tabla_productos():

  print("\n================== INVENTARIO ==================")
  print("N° PRODUCTO       PRECIO   STOCK")
  print("------------------------------------------------")

  for i in range(len(nombres_productos)):

    print(
      f"{i + 1:<3} {nombres_productos[i]:<22} "
      f"S/. {precios_productos[i]:<8.2f} "
      f"{stock_productos[i]}"
    )

  print("------------------------------------------------")

# ==========================
# CREATE(agregar_producto)
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
# READ(mostar_producto)
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
#Esta función sirve para cambiar el stock de un producto.
#Primero pide el nombre del producto.
#Si lo encuentra, pide el nuevo stock.
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
#Esta función sirve para eliminar un producto del inventario.
#Busca el producto por su nombre.
#Si lo encuentra, elimina sus datos de todas las listas usando
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
#Esta función sirve para registrar la venta de un producto.
#Primero pide el nombre del producto vendido.
#Si el producto existe, pide la cantidad vendida.
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