from modelos.producto import Producto
from modelos.cliente import Cliente
from typing import List, Optional

class Restaurante:
    def __init__(self):
        # Contenedores privados para guardar los datos mientras la app esté abierta
        self._catalogo_productos: List[Producto] = []
        self._registro_clientes: List[Cliente] = []

    # Operaciones para los Productos
    def registrar_producto(self, item: Producto) -> None:
        self._catalogo_productos.append(item)

    def listar_productos(self) -> List[Producto]:
        return self._catalogo_productos

    def buscar_producto(self, termino_busqueda: str) -> Optional[Producto]:
        for prod in self._catalogo_productos:
            # Comparamos ignorando diferencias entre mayúsculas y minúsculas
            if prod.nombre.lower() == termino_busqueda.lower().strip():
                return prod
        return None

    # Operaciones para los Clientes
    def registrar_cliente(self, usuario: Cliente) -> None:
        self._registro_clientes.append(usuario)

    def listar_clientes(self) -> List[Cliente]:
        return self._registro_clientes

    def buscar_cliente(self, codigo_id: str) -> Optional[Cliente]:
        for cli in self._registro_clientes:
            if cli.id_cliente.strip() == codigo_id.strip():
                return cli
        return None