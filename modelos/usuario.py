class Usuario:
    def __init__(self, identificacion: str, nombre: str, email: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.email = email

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "email": self.email
        }