from servicios.restaurante import Restaurante

# Uso de TUPLA: Datos inmutables que no cambian durante la ejecución
OPCIONES_MENU: tuple[str, ...] = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías de productos",
    "Salir"
)

# Uso de DICCIONARIO: Relación clave -> valor para asociar la opción con su descripción
DESCRIPCION_OPCIONES: dict[str, str] = {
    "1": "Permite ingresar un nuevo producto al restaurante.",
    "2": "Busca un producto registrado mediante su código.",
    "3": "Modifica los datos de un producto existente.",
    "4": "Elimina un producto del sistema.",
    "5": "Muestra todos los productos registrados.",
    "6": "Registra una nueva persona en el sistema.",
    "7": "Muestra todos los usuarios registrados.",
    "8": "Obtiene la lista de categorías sin duplicados.",
    "9": "Cierra la aplicación."
}

def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("      SISTEMA DE GESTIÓN RESTAURANTE")
    print("=" * 40)
    for i, opcion in enumerate(OPCIONES_MENU, start=1):
        if i == 6 or i == 8:
            print("-" * 40)
        print(f"{i}. {opcion}")
    print("=" * 40)

def registrar_producto_consola(servicio: Restaurante) -> None:
    print("\n--- Registrar Nuevo Producto ---")
    codigo = input("Ingrese el código del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría (Ej. Bebidas, Platos): ").strip()
    
    try:
        precio = float(input("Ingrese el precio: ").strip())
        if precio <= 0:
            print("El precio debe ser un número positivo.")
            return

        exito = servicio.registrar_producto(codigo, nombre, categoria, precio)
        if exito:
            print("¡Producto registrado con éxito!")
        else:
            print("Error: Ya existe un producto registrado con ese código.")
    except ValueError:
        print("Error: El precio ingresado no es un número válido.")

def buscar_producto_consola(servicio: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    producto = servicio.buscar_producto(codigo)
    
    if producto:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("No se encontró ningún producto con ese código.")

def actualizar_producto_consola(servicio: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    
    producto_actual = servicio.buscar_producto(codigo)
    if not producto_actual:
        print("No existe un producto con el código ingresado.")
        return

    print(f"Producto actual: {producto_actual}")
    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
    nueva_categoria = input("Ingrese la nueva categoría: ").strip()
    
    try:
        nuevo_precio = float(input("Ingrese el nuevo precio: ").strip())
        if nuevo_precio <= 0:
            print("El precio debe ser positivo.")
            return

        if servicio.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio):
            print("¡Producto actualizado correctamente!")
    except ValueError:
        print("Error: Ingrese un valor numérico para el precio.")

def eliminar_producto_consola(servicio: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    
    if servicio.eliminar_producto(codigo):
        print("¡Producto eliminado exitosamente!")
    else:
        print("No se encontró ningún producto con ese código.")

def listar_productos_consola(servicio: Restaurante) -> None:
    print("\n--- Lista de Productos ---")
    productos = servicio.listar_productos()
    
    if not productos:
        print("No hay productos registrados en el sistema.")
    else:
        for p in productos:
            print(p)

def registrar_usuario_consola(servicio: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = input("Ingrese la identificación (cédula/ID): ").strip()
    nombre = input("Ingrese el nombre completo: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()
    
    if servicio.registrar_usuario(identificacion, nombre, correo):
        print("¡Usuario registrado con éxito!")
    else:
        print("Error: Ya existe un usuario con esa identificación.")

def listar_usuarios_consola(servicio: Restaurante) -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = servicio.listar_usuarios()
    
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for u in usuarios:
            print(u)

def mostrar_categorias_consola(servicio: Restaurante) -> None:
    print("\n--- Categorías Únicas Registradas ---")
    categorias = servicio.obtener_categorias_unicas()
    
    if not categorias:
        print("No hay categorías registradas todavía.")
    else:
        for cat in categorias:
            print(f"- {cat}")

def main() -> None:
    servicio = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()
        
        if opcion in DESCRIPCION_OPCIONES:
            print(f"\n[Info]: {DESCRIPCION_OPCIONES[opcion]}")

        if opcion == "1":
            registrar_producto_consola(servicio)
        elif opcion == "2":
            buscar_producto_consola(servicio)
        elif opcion == "3":
            actualizar_producto_consola(servicio)
        elif opcion == "4":
            eliminar_producto_consola(servicio)
        elif opcion == "5":
            listar_productos_consola(servicio)
        elif opcion == "6":
            registrar_usuario_consola(servicio)
        elif opcion == "7":
            listar_usuarios_consola(servicio)
        elif opcion == "8":
            mostrar_categorias_consola(servicio)
        elif opcion == "9":
            print("\nSaliendo del sistema de restaurante... ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione un número entre 1 y 9.")

if __name__ == "__main__":
    main()