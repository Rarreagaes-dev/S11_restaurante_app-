from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import (
    cargar_productos,
    guardar_productos,
    cargar_usuarios,
    guardar_usuarios,
    cargar_ventas,
    guardar_ventas
)

class Restaurante:
    def __init__(self):
        self._productos = cargar_productos()
        self._usuarios = cargar_usuarios()
        self._ventas = cargar_ventas()

    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int = 0) -> bool:
        if self.buscar_producto(codigo):
            return False
        producto = Producto(codigo, nombre, precio, stock)
        self._productos.append(producto)
        guardar_productos(self._productos)
        return True

    def buscar_producto(self, codigo: str):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_usuario(self, identificacion: str, nombre: str, email: str) -> bool:
        if self.buscar_usuario(identificacion):
            return False
        usuario = Usuario(identificacion, nombre, email)
        self._usuarios.append(usuario)
        guardar_usuarios(self._usuarios)
        return True

    def buscar_usuario(self, identificacion: str):
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        try:
            producto.vender(cantidad)
        except ValueError:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)

        guardar_ventas(self._ventas)
        guardar_productos(self._productos)

        return True

    def consultar_ventas_por_usuario(self, identificacion_usuario: str):
        ventas_usuario = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    def listar_productos(self):
        return self._productos

    def listar_usuarios(self):
        return self._usuarios

    def listar_ventas(self):
        return self._ventas