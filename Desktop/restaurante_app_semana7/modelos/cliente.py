from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self) -> str:
        return f"Cliente ID [{self.id_cliente}]: {self.nombre} (Contacto: {self.correo})"