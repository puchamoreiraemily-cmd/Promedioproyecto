

```bash
cat << 'EOF' > README.md
# Biblioteca App

Proyecto académico en Python para practicar Programación Orientada a Objetos y estructuras de datos en memoria.

## Estructura del Proyecto

```text
biblioteca_app/
├── modelos/
│   ├── __init__.py
│   ├── libro.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── biblioteca.py
├── main.py
└── README.md

```

## Ejecución

```bash
python main.py

```

## Responsabilidades

* **`modelos/libro.py`**: Clase `Libro` y validaciones principales.
* **`modelos/usuario.py`**: Clase `Usuario` y atributos de lectores.
* **`servicios/biblioteca.py`**: Administra las colecciones y la lógica del sistema (`Biblioteca`).
* **`main.py`**: Menú de consola y flujo de interacción.

## Justificación de Estructuras de Datos

* **`list`** (`_libros`, `_usuarios`): Colecciones dinámicas de objetos. Permite modificar, recorrer y administrar elementos con `append()`, `remove()`, `len()` y ciclos `for`.
* **`tuple`** (`OPCIONES_MENU`): Colección fija e inmutable en `main.py` para evitar alteraciones en las opciones del menú durante la ejecución.
* **`dict`**: Relaciones clave $\to$ valor. Mapea opciones a funciones en `main.py` y códigos de libros a IDs de usuarios prestatarios en `_prestamos`.
* **`set`** (`obtener_categorias_unicas()`): Colección que elimina automáticamente duplicados para obtener un listado limpio de categorías.

## Menú Principal

1. **Gestión de Libros:** Registrar, buscar, actualizar, eliminar y listar.
2. **Gestión de Usuarios:** Registrar, buscar, actualizar, eliminar y listar.
3. **Servicios Especiales:** Prestar libro a usuario y listar categorías únicas.

## Objetivo Pedagógico

Demostrar cómo la clase `Biblioteca` (`servicios/`) administra colecciones de objetos (`Libro`, `Usuario`) utilizando estructuras de datos nativas en memoria.
EOF

```

```