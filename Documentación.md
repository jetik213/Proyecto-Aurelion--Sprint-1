# DOCUMENTACIÓN.md

## 1. Tema del Proyecto
"Chatbot Interactivo para el Minimarket Aurelion"
El minimarket Aurelion opera en un mercado minorista competitivo, donde la eficiencia en la gestión de inventario y la fidelización de clientes son cruciales para la supervivencia. 
Este minimarket opera con una base de datos maestra de 100 clientes únicos y ha registrado 120 transacciones de venta entre enero y junio de 2024, acumulando un total de ingresos de $2,651,417. Si bien la tienda ha logrado una fidelización efectiva con un segmento de alto valor, el negocio enfrenta un riesgo operativo significativo debido a la extrema volatilidad de sus ingresos, evidenciado por la fuerte caída en abril que fue seguida por un pico de recuperación en mayo, lo que dificulta la planificación del flujo de caja y la gestión de inventario. Financieramente, la categoría de Limpieza es actualmente el principal motor de ingresos de la tienda superando a Alimentos, y el Desodorante Aerosol figura como el producto de mayor valor en ventas. Operacionalmente, Aurelion opera en al menos cuatro ciudades distintas y su dependencia del Efectivo como el medio de pago más utilizado (37 transacciones) añade complejidad y riesgo en la gestión de cobros en comparación con las transacciones digitales.
---

## 2. Problema
El problema central del minimarket Aurelion es la inaccesibilidad total a su propia información de negocio. Actualmente, todos los datos vitales de la empresa —clientes, productos y transacciones— se encuentran aislados en archivos de Excel en crudo, sin ningún tipo de procesamiento, documentación o interfaz gráfica que permita su consulta. Esto crea un "desierto de información", donde los dueños o gerentes son incapaces de responder preguntas críticas para la estrategia del negocio de manera ágil. La falta de un sistema para analizar la estructura, los tipos de datos, características, entre otros, de las bases de datos, hace que el proceso manual sea lento y fragmentado, lo que imposibilita la toma de decisiones informadas en tiempo real. En resumen, el problema es la carencia absoluta de un canal interactivo y centralizado que exponga las características de sus bases de datos de forma sencilla para los interesados.
---

## 3. Solución Propuesta
Para resolver la carencia de un canal de información, se propone el desarrollo de un chatbot que funcionará como un asistente de consulta interactivo y centralizado. Este chatbot está diseñado para interpretar las solicitudes del usuario a través de un menú de opciones predefinidas, atacando directamente el problema de la inaccesibilidad de la información. De esta manera, la solución convierte los datos aislados de los archivos Excel en conocimiento estructurado y accesible bajo demanda, permitiendo que cualquier interesado pueda comprender el panorama completo del proyecto de forma instantánea y sin necesidad de conocimientos técnicos.
---

## 4. Características set de datos

A continuación se detalla la estructura, los tipos de datos y la descripción de cada tabla.

### 4.1. Base de Datos: Clientes
* **Fuente:** `clientes.xlsx - clientes.csv`
* **Definición:** Tabla maestra que contiene el registro único de todos los clientes de la tienda.
* **Columnas:** El catálogo está compuesto por las siguientes columnas:
1.  **`id_cliente`**
    * **Tipo y Naturaleza:** Entero, Cuantitativo.
    * **Llave:** **Primaria (PK)**.
    * **Descripción:** Es el **identificador numérico único** asignado a cada cliente.
2.  **`nombre_cliente`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Descripción:** Contiene el nombre y apellido completo del cliente.
3.  **`email`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Descripción:** Almacena la dirección de correo electrónico del cliente.
4.  **`ciudad`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Descripción:** Indica la ciudad de residencia del cliente.
5.  **`fecha_alta`**
    * **Tipo y Naturaleza:** Fecha, Cualitativo.
    * **Descripción:** Registra la fecha en la que el cliente se registró por primera vez en el sistema.

* **Nota: Todos los campos provienen de origen **Primario** y son de estructura **Estructurada**.**
---

### 4.2. Base de Datos: Productos
* **Fuente:** `productos.xlsx - productos.csv`
* **Definición:** Catálogo maestro que describe cada uno de los productos disponibles para la venta.
* **Columnas:** El catálogo está compuesto por las siguientes columnas:
1.  **`id_producto`**
    * **Tipo y Naturaleza:** Entero, Cuantitativo.
    * **Llave:** **Primaria (PK)**.
    * **Descripción:** Es el **identificador numérico único** asignado a cada producto.
2.  **`nombre_producto`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Descripción:** Contiene el nombre comercial del producto.
3.  **`categoria`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Descripción:** Define la categoría a la que pertenece el producto (ej. Alimentos, Limpieza).
4.  **`precio_unitario`**
    * **Tipo y Naturaleza:** Decimal, Cuantitativo.
    * **Descripción:** Indica el precio de venta por una unidad del producto.

* **Nota: Todos los campos provienen de origen **Primario** y son de estructura **Estructurada**.**
---

### 4.3. Base de Datos: Ventas
* **Fuente:** `ventas.xlsx - ventas.csv`
* **Definición:** Tabla transaccional que funciona como encabezado de cada orden de compra.
* **Columnas:** El catálogo está compuesto por las siguientes columnas:
1.  **`id_venta`**
    * **Tipo y Naturaleza:** Entero, Cuantitativo.
    * **Llave:** **Primaria (PK)**.
    * **Descripción:** Es el **identificador numérico único** asignado a cada transacción de venta.
2.  **`fecha`**
    * **Tipo y Naturaleza:** Fecha, Cualitativo.
    * **Origen:** Primario.
    * **Descripción:** Indica la fecha exacta en la que se procesó la venta.
3.  **`id_cliente`**
    * **Tipo y Naturaleza:** Entero, Cuantitativo.
    * **Llave:** **Foránea (FK)**.
    * **Origen:** Primario.
    * **Descripción:** Identificador que **referencia al cliente** en la tabla **Clientes**.
4.  **`nombre_cliente`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Origen:** Secundario.
    * **Descripción:** Nombre del cliente, incluido como un **dato denormalizado** para facilitar la consulta rápida sin necesidad de unir tablas.
5.  **`email`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Origen:** Secundario.
    * **Descripción:** Dirección de correo electrónico del cliente, incluido como un **dato denormalizado** para facilitar la consulta rápida.
6.  **`medio_pago`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Origen:** Primario.
    * **Descripción:** Detalla el método utilizado para el pago de la compra (ej. tarjeta, QR, efectivo, etc.).

* **Nota: Todos los campos provienen de origen **Primario** y son de estructura **Estructurada**.**
---

### 4.4. Base de Datos: Detalle de Ventas
* **Fuente:** `detalle_ventas.xlsx - detalle_ventas.csv`
* **Definición:** Tabla transaccional que desglosa los productos y cantidades de cada venta.
* **Columnas:** El catálogo está compuesto por las siguientes columnas:
1.  **`id_venta`**
    * **Tipo y Naturaleza:** Entero, Cuantitativo.
    * **Llave:** **Foránea (FK)**.
    * **Origen:** Primario.
    * **Descripción:** Es la clave que **referencia a la venta** en la tabla **Ventas** (encabezado de la orden).
2.  **`id_producto`**
    * **Tipo y Naturaleza:** Entero, Cuantitativo.
    * **Llave:** **Foránea (FK)**.
    * **Origen:** Primario.
    * **Descripción:** Es la clave que **referencia al producto** en la tabla **Productos** (catálogo).
3.  **`nombre_producto`**
    * **Tipo y Naturaleza:** Texto, Cualitativo.
    * **Origen:** Secundario.
    * **Descripción:** Nombre del producto, incluido como un **dato denormalizado** para facilitar la consulta.
4.  **`cantidad`**
    * **Tipo y Naturaleza:** Entero, Cuantitativo.
    * **Origen:** Primario.
    * **Descripción:** Representa el número de unidades vendidas de ese producto específico dentro de la venta.
5.  **`precio_unitario`**
    * **Tipo y Naturaleza:** Decimal, Cuantitativo.
    * **Origen:** Secundario.
    * **Descripción:** Precio del producto registrado **al momento de la venta** (dato denormalizado, capturado para mantener el histórico del precio).
6.  **`importe`**
    * **Tipo y Naturaleza:** Decimal, Cuantitativo.
    * **Origen:** Secundario.
    * **Descripción:** Monto total calculado para esta línea de producto (resultado de multiplicar **`cantidad`** por **`precio_unitario`**).

* **Nota: Todos los campos provienen de origen **Primario** y son de estructura **Estructurada**.**
---

## 5. Pasos



## 6. Diagrama de flujo


## 7. Pseudocódigo


## 8. Ejecutar programa

