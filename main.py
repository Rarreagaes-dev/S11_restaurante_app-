from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n=== RESTAURANTE APP - SEMANA 11 ===")
    print("1. Registrar producto")
    print("2. Registrar usuario")
    print("3. Vender producto")
    print("4. Consultar ventas por usuario")
    print("5. Listar productos")
    print("6. Listar usuarios")
    print("7. Listar ventas")
    print("8. Salir")

def main():
    sistema = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            stock = int(input("Stock inicial: "))
            if sistema.registrar_producto(codigo, nombre, precio, stock):
                print("Producto registrado correctamente.")
            else:
                print("Error: el producto ya existe.")

        elif opcion == "2":
            identificacion = input("Identificación del usuario: ")
            nombre = input("Nombre del usuario: ")
            email = input("Email del usuario: ")
            if sistema.registrar_usuario(identificacion, nombre, email):
                print("Usuario registrado correctamente.")
            else:
                print("Error: el usuario ya existe.")

        elif opcion == "3":
            identificacion_usuario = input("Identificación del usuario: ")
            codigo_producto = input("Código del producto: ")
            cantidad = int(input("Cantidad a vender: "))
            if sistema.vender_producto(codigo_producto, identificacion_usuario, cantidad):
                print("Venta realizada correctamente.")
            else:
                print("Venta rechazada: usuario, producto o cantidad no válidos, o stock insuficiente.")

        elif opcion == "4":
            identificacion_usuario = input("Identificación del usuario: ")
            ventas = sistema.consultar_ventas_por_usuario(identificacion_usuario)
            if not ventas:
                print("El usuario no tiene ventas registradas.")
            else:
                print(f"\nVentas del usuario {identificacion_usuario}:")
                for venta in ventas:
                    producto = sistema.buscar_producto(venta.producto_codigo)
                    nombre_producto = producto.nombre if producto else "Producto no encontrado"
                    print(f"- Producto: {venta.producto_codigo} | {nombre_producto} | Cantidad: {venta.cantidad}")

        elif opcion == "5":
            print("\nLista de productos:")
            for p in sistema.listar_productos():
                print(f"{p.codigo} - {p.nombre} - ${p.precio:.2f} - Stock: {p.stock}")

        elif opcion == "6":
            print("\nLista de usuarios:")
            for u in sistema.listar_usuarios():
                print(f"{u.identificacion} - {u.nombre} - {u.email}")

        elif opcion == "7":
            print("\nLista de ventas:")
            for v in sistema.listar_ventas():
                print(f"Usuario: {v.usuario_id} | Producto: {v.producto_codigo} | Cantidad: {v.cantidad}")

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()