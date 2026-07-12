class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Pasamos los parámetros por los setters para activar las validaciones de inmediato
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # --- Gestión del Nombre ---
    @property
    def nombre(self) -> str:
        return self._txt_nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Por favor, ingresa un nombre válido para el producto.")
        self._txt_nombre = valor.strip()

    # --- Gestión de la Categoría ---
    @property
    def categoria(self) -> str:
        return self._txt_categoria

    @categoria.setter
    def categoria(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("La categoría no puede quedarse en blanco.")
        self._txt_categoria = valor.strip()

    # --- Gestión del Precio ---
    @property
    def precio(self) -> float:
        return self._num_precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio asignado debe ser una cantidad mayor a 0.")
        self._num_precio = valor

    # --- Gestión de Disponibilidad ---
    @property
    def disponible(self) -> bool:
        return self._en_stock

    @disponible.setter
    def disponible(self, valor: bool):
        self._en_stock = bool(valor)

    def mostrar_informacion(self) -> str:
        estado_actual = "Disponible para la venta" if self.disponible else "Fuera de stock"
        return f"[{self.categoria}] {self.nombre} -> Costo: ${self.precio:.2f} ({estado_actual})"