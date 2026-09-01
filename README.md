
---

# Restaurante App - Semana 11 (POO)

**Estudiante:** Merlinthon Wilfrido España Carbo  
**Asignatura:** Programación Orientada a Objetos  

## Descripción
Evolución del sistema `restaurante_app`. Esta versión incorpora la gestión de **Ventas**, relacionando Usuarios con Productos, controlando el **stock** de inventario y asegurando la **persistencia** de toda la información mediante archivos JSON.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/              # Archivos JSON (productos, usuarios, ventas)
├── modelos/            # Clases Producto, Usuario y Venta
├── servicios/          # Lógica de negocio y persistencia
├── main.py             # Menú principal e interacción
└── README.md           # Documentación
```

## Responsabilidades
- **modelos/**: Define las entidades. `Producto` maneja stock, `Usuario` la identidad y `Venta` vincula a ambos con una cantidad específica.
- **servicios/restaurante.py**: Administra colecciones, ejecuta validaciones de stock y reglas de negocio.
- **servicios/archivo_servicio.py**: Centraliza la carga y guardado de datos en formato JSON.
- **main.py**: Gestiona la entrada del usuario sin manipular directamente las colecciones.

## Operaciones y Relaciones
- **Venta (Usuario + Producto):** Se registra una venta solo si el usuario y producto existen, y si el stock es suficiente.
- **Gestión de Stock:** Al realizar una venta, el stock del producto disminuye automáticamente. Se impide que el stock sea negativo.
- **Consulta:** Permite filtrar y listar todas las ventas realizadas por un usuario específico.

## Persistencia JSON
El sistema garantiza que los datos se mantengan al cerrar la aplicación:
- **productos.json**: Almacena catálogo y stock actualizado.
- **usuarios.json**: Almacena el registro de clientes/usuarios.
- **ventas.json**: Almacena el histórico de transacciones.

## Manejo de Excepciones
Se controlan errores críticos para evitar el cierre inesperado:
- `FileNotFoundError`: Inicia con colecciones vacías si no hay archivos.
- `JSONDecodeError`: Maneja archivos con formato corrupto.
- `ValueError`: Valida que cantidades y stock sean lógicos (números positivos).

## Instrucciones de Ejecución
1. Ubicarse en la raíz del proyecto.
2. Ejecutar el comando:
   ```bash
   python main.py
   ```

## Pruebas Realizadas
1. **Registro:** Se crearon usuarios y productos con stock inicial.
2. **Venta Válida:** Se procesó una venta; el stock disminuyó y se generó el registro en `ventas.json`.
3. **Validación de Stock:** Se intentó vender una cantidad superior al stock y el sistema rechazó la operación correctamente.
4. **Persistencia:** Se cerró el programa, se reinició y se comprobó que los productos, usuarios y ventas anteriores fueron cargados correctamente.

---

### Reflexión
El uso de **colecciones de objetos** facilita la representación de procesos del mundo real. La separación de responsabilidades (Modelos/Servicios) permite que la persistencia JSON sea transparente para el usuario, asegurando que la lógica de negocio (como el control de stock) se mantenga íntegra e independiente de la interfaz.