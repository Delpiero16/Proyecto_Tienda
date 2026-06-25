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


