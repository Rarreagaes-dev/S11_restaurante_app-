class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if self.stock < cantidad:
            raise ValueError("Stock insuficiente.")
        self.stock -= cantidad

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }