# 🍔 Sistema de Gestión de Restaurante - Semana 7

**Estudiante:** Emily Pucha  
**Asignatura:** Programación Orientada a Objetos  

---

## 📝 1. Descripción del Sistema
Este sistema es una aplicación de consola diseñada para administrar la operación básica de un restaurante mediante el manejo de dos entidades principales: **Productos** (platillos y bebidas disponibles) y **Clientes** registrados. El programa permite realizar altas, búsquedas específicas y listados globales en tiempo real. La persistencia de la información se maneja dinámicamente en la memoria RAM a través de una clase de servicio especializada, evitando por completo el uso de datos fijos o predefinidos en el código fuente.

---

## 📁 2. Estructura del Proyecto
El proyecto se organizó bajo una arquitectura modular por capas, separando las responsabilidades de la interfaz, la lógica de almacenamiento y las reglas de negocio:

*   **`restaurante_app/`**: Carpeta raíz del proyecto.
    *   **`modelos/`**: Capa que define la estructura de los datos del sistema.
        *   `__init__.py`: Archivo vacío necesario para empaquetar el módulo.
        *   `producto.py`: Contiene la lógica, encapsulamiento y reglas de la entidad Producto.
        *   `cliente.py`: Contiene la estructura simplificada de la entidad Cliente.
    *   **`servicios/`**: Capa encargada de la lógica de negocio.
        *   `__init__.py`: Inicializador del módulo de servicios.
        *   `restaurante.py`: Clase de servicio que controla y opera las listas de datos en memoria.
    *   **`main.py`**: Punto de arranque de la aplicación. Maneja el menú de usuario y las capturas de teclado.

---

## 🏗️ 3. Uso del Constructor en la Clase Producto
En la clase `Producto` se implementó un **constructor tradicional (`__init__`)**. Este método se encarga de recibir los parámetros iniciales (nombre, categoría, precio y disponibilidad) al momento de instanciar el objeto. Para garantizar la seguridad del sistema, las asignaciones dentro del constructor se realizan llamando directamente a las propiedades públicas, obligando a que cualquier dato nuevo pase por los filtros de validación obligatorios antes de ser almacenado en los atributos privados.

---

## 🔒 4. Uso de @property y @setter
Se utilizaron los decoradores `@property` (como getter) y `@setter` en la clase `Producto` para aplicar el principio de encapsulamiento. Esto permite interceptar la lectura y modificación de las variables internas (`_txt_nombre`, `_txt_categoria`, `_num_precio`), aplicando validaciones críticas en tiempo de ejecución:
*   **Validación de texto:** Evita que el nombre o la categoría se registren vacíos o con espacios en blanco.
*   **Validación numérica:** Restringe el precio para asegurar que sea estrictamente una cantidad mayor a cero, lanzando un error (`ValueError`) si la condición no se cumple.

---

## 📊 5. Uso de @dataclass en la Clase Cliente
Para la entidad `Cliente` se implementó el decorador moderno `@dataclass`. Dado que esta clase tiene como único fin almacenar datos básicos (nombre, correo electrónico e identificador único), `@dataclass` optimiza el desarrollo autogenerando de forma limpia el método constructor `__init__`, la representación en texto y los métodos de comparación detrás de escena, reduciendo las líneas de código repetitivo de forma drástica.

---

## 💻 6. Descripción del Menú Interactivo
El archivo `main.py` actúa como la interfaz del sistema mediante un bucle continuo (`while True`) que despliega el menú obligatorio por consola:
*   **Opciones 1, 2 y 3:** Permiten registrar un producto capturando sus datos por teclado, listar todos los productos guardados en el catálogo y buscar un artículo específico por su nombre (ignorando mayúsculas y minúsculas).
*   **Opciones 4, 5 y 6:** Permiten registrar un cliente capturando sus datos, listar los clientes asociados y localizar a un usuario mediante su código ID único.
*   **Opción 7:** Rompe el ciclo de ejecución y cierra el programa de manera limpia.

---

## 🧠 7. Reflexión: Importancia de crear objetos a partir de datos del usuario
La creación de objetos a partir de datos dinámicos ingresados por el usuario mediante `input()` representa el puente real entre el software y el entorno operativo del negocio. En el desarrollo de software profesional, los sistemas no pueden depender de datos quemados en el código. 

Permitir que el usuario defina los atributos en tiempo de ejecución obliga al programa a ser flexible, adaptable y robusto. Además, este flujo evidencia la verdadera utilidad de la Programación Orientada a Objetos: el código actúa como un molde genérico (Clase) que cobra vida y utilidad únicamente cuando interactúa con las necesidades cambiantes del mundo real, transformando texto plano de una consola en entidades de negocio validadas y estructuradas.