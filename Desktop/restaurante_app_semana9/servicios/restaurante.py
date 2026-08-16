from typing import Optional
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """Servicio para gestionar los productos, usuarios y operaciones del restaurante."""

    def __init__(self) -> None:
        # Uso de LISTA: Colecciones dinámicas de objetos
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

    # --- Gestión de Productos ---

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> bool:
        # Validar que no exista un producto con el mismo código
        if self.buscar_producto(codigo) is not None:
            return False
        
        nuevo_producto = Producto(codigo, nombre, categoria, precio)
        self.productos.append(nuevo_producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.codigo.lower() == codigo.lower():
                return producto
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is not None:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is not None:
            self.productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> list[Producto]:
        return self.productos

    # --- Gestión de Usuarios ---

    def registrar_usuario(self, identificacion: str, nombre: str, correo: str) -> bool:
        # Validar que no se repita la identificación
        if self.buscar_usuario(identificacion) is not None:
            return False
        
        nuevo_usuario = Usuario(identificacion, nombre, correo)
        self.usuarios.append(nuevo_usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    # --- Operación con Conjunto ---

    def obtener_categorias_unicas(self) -> set[str]:
        # Uso de CONJUNTO: Obtiene categorías sin repetir elementos
        categorias: set[str] = set()
        for producto in self.productos:
            categorias.add(producto.categoria.strip().title())
        return categorias