import json
import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

DATOS_FOLDER = "datos"

def _asegurar_carpeta_datos():
    if not os.path.exists(DATOS_FOLDER):
        os.makedirs(DATOS_FOLDER)

def guardar_productos(productos):
    _asegurar_carpeta_datos()
    ruta = os.path.join(DATOS_FOLDER, "productos.json")
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump([p.to_dict() for p in productos], archivo, indent=4, ensure_ascii=False)

def cargar_productos():
    ruta = os.path.join(DATOS_FOLDER, "productos.json")
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Producto(**d) for d in datos]
    except json.JSONDecodeError:
        return []
    except PermissionError:
        return []

def guardar_usuarios(usuarios):
    _asegurar_carpeta_datos()
    ruta = os.path.join(DATOS_FOLDER, "usuarios.json")
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump([u.to_dict() for u in usuarios], archivo, indent=4, ensure_ascii=False)

def cargar_usuarios():
    ruta = os.path.join(DATOS_FOLDER, "usuarios.json")
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Usuario(**d) for d in datos]
    except json.JSONDecodeError:
        return []
    except PermissionError:
        return []

def guardar_ventas(ventas):
    _asegurar_carpeta_datos()
    ruta = os.path.join(DATOS_FOLDER, "ventas.json")
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump([v.to_dict() for v in ventas], archivo, indent=4, ensure_ascii=False)

def cargar_ventas():
    ruta = os.path.join(DATOS_FOLDER, "ventas.json")
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Venta(**d) for d in datos]
    except json.JSONDecodeError:
        return []
    except PermissionError:
        return []