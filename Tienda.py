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