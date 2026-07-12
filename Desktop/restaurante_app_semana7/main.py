from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def iniciar_aplicacion():
    # Instancia del administrador del negocio
    gestion_local = Restaurante()

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("----------------------------------------")
        print("4. Registrar cliente")
        print("5. Listar clientes")
        print("6. Buscar cliente")
        print("----------------------------------------")
        print("7. Salir")
        print("========================================")
        
        opcion = input("Por favor, elija una opción (1-7): ").strip()

        if opcion == "1":
            print("\n>> NUEVO REGISTRO DE PRODUCTO <<")
            try:
                nom = input("Nombre del platillo/bebida: ")
                cat = input("Categoría (Entradas, Bebidas, etc.): ")
                pre = float(input("Precio de venta ($): "))
                
                # Se construye la entidad con los datos del teclado
                objeto_producto = Producto(nom, cat, pre)
                gestion_local.registrar_producto(objeto_producto)
                print("-> Producto guardado en el catálogo.")
            except ValueError as error:
                print(f"No se pudo guardar: {error}")

        elif opcion == "2":
            print("\n>> CATÁLOGO DE PRODUCTOS ACTUAL <<")
            lista = gestion_local.listar_productos()
            if not lista:
                print("Aún no has registrado ningún producto.")
            else:
                for p in lista:
                    print(p.mostrar_informacion())

        elif opcion == "3":
            print("\n>> LOCALIZAR PRODUCTO <<")
            buscar = input("Nombre del artículo que deseas buscar: ")
            resultado = gestion_local.buscar_producto(buscar)
            if resultado:
                print("\nResultado de la búsqueda:")
                print(resultado.mostrar_informacion())
            else:
                print("No se encontró ningún artículo con ese nombre.")

        elif opcion == "4":
            print("\n>> NUEVO REGISTRO DE CLIENTE <<")
            nom_cli = input("Nombre completo: ").strip()
            mail_cli = input("Correo electrónico: ").strip()
            id_cli = input("Código de identificación único: ").strip()
            
            if not nom_cli or not mail_cli or not id_cli:
                print("Error: Todos los datos del cliente son requeridos obligatoriamente.")
                continue

            objeto_cliente = Cliente(nombre=nom_cli, correo=mail_cli, id_cliente=id_cli)
            gestion_local.registrar_cliente(objeto_cliente)
            print("-> Cliente agregado al sistema correctamente.")

        elif opcion == "5":
            print("\n>> REGISTRO DE CLIENTES ASOCIADOS <<")
            lista_cli = gestion_local.listar_clientes()
            if not lista_cli:
                print("No existen registros de clientes todavía.")
            else:
                for c in lista_cli:
                    print(c.mostrar_informacion())

        elif opcion == "6":
            print("\n>> LOCALIZAR CLIENTE <<")
            buscar_id = input("Escriba el ID del cliente: ")
            resultado_cli = gestion_local.buscar_cliente(buscar_id)
            if resultado_cli:
                print("\nResultado de la búsqueda:")
                print(resultado_cli.mostrar_informacion())
            else:
                print("El identificador proporcionado no coincide con ningún cliente.")

        elif opcion == "7":
            print("\nCerrando el sistema del restaurante. ¡Que tenga un excelente día!")
            break
        else:
            print("Opción no válida. Intente con un número que esté dentro del rango 1 al 7.")

if __name__ == "__main__":
    iniciar_aplicacion()