# DOCUMENTACIÓN.md

## 1. Tema del Proyecto
Análisis de Ventas y Comportamiento del Cliente para un Supermercado.

---

### 2. Problema
La gerencia del supermercado necesita realizar un **análisis cuantitativo y sistemático** de sus operaciones para optimizar el inventario, personalizar campañas de marketing y mejorar la rentabilidad. El proceso actual de toma de decisiones se basa en intuición y reportes manuales, lo que impide responder con agilidad y precisión a preguntas clave del negocio:

* **Rendimiento de Productos:** ¿Cuáles son nuestros productos más y menos vendidos en términos de cantidad e ingresos generados?
* **Segmentación de Clientes:** ¿Quiénes son nuestros clientes más valiosos (top clientes por gasto total) y cuál es su frecuencia de compra?
* **Desempeño Geográfico:** ¿En qué ciudades se concentra la mayor cantidad de ventas y el mayor valor de compra?
* **Eficiencia Operativa:** ¿Cuál es el método de pago más utilizado y cómo se distribuyen las ventas a lo largo del mes y del año?

La falta de un proceso automatizado para obtener estas respuestas resulta en una gestión de inventario ineficiente y en la pérdida de oportunidades para fidelizar a los clientes más importantes.

---

### 3. Solución Propuesta
Se propone el desarrollo de un **script de análisis de datos en Python**, utilizando las librerías **Pandas** y **NumPy**, para procesar y extraer insights de las bases de datos proporcionadas. Este enfoque reemplaza la necesidad de un dashboard con un análisis de código robusto, automatizado y repetible.

El proyecto se ejecutará en las siguientes fases:

1.  **Consolidación de Datos:**
    * Cargar los cuatro archivos CSV (`clientes`, `productos`, `ventas`, `detalle_ventas`) en DataFrames de Pandas.
    * Realizar la limpieza de datos (manejo de nulos, corrección de tipos de datos) y unificar la información en un único DataFrame analítico principal.

2.  **Análisis y Cómputo de Métricas:**
    * Utilizar la potencia de Pandas para realizar agrupaciones, agregaciones y cálculos que respondan directamente a las preguntas del negocio. Se generarán los siguientes análisis:
        * **Top 5 Productos:** Un ranking de productos por `cantidad` vendida y por `importe` total.
        * **Top 5 Clientes:** Un listado de los clientes con mayor gasto acumulado.
        * **Ventas por Ciudad:** Un resumen del `importe` total de ventas agrupado por ciudad.
        * **Distribución de Pagos:** Un conteo de la frecuencia de uso de cada `medio_pago`.

3.  **Generación de Reportes:**
    * Como resultado principal, el script generará una serie de gráficos para la experimentación y el análisis visual de los datos. Utilizando librerías como Matplotlib y Seaborn, se crearán las siguientes visualizaciones:
        * Un **gráfico de barras** para mostrar las ventas del "Top 5 Productos".
        * Un **gráfico de barras** para visualizar el gasto total del "Top 5 Clientes".
        * Un **gráfico de barras** comparando las ventas totales por ciudad.
        * Un **gráfico circular (pie chart)** para ilustrar la proporción de cada método de pago.

Esta solución proveerá respuestas concretas y cuantificables a los problemas de negocio, creando un flujo de trabajo que puede ser ejecutado periódicamente para monitorear el desempeño de la empresa.

***

## Descripción de las Bases de Datos

A continuación se detalla la estructura, los tipos de datos y la descripción de cada tabla.

### 1. Base de Datos: Clientes
* **Fuente:** `clientes.xlsx - clientes.csv.csv`
* **Definición:** Tabla maestra que contiene el registro único de todos los clientes de la tienda.

| Nombre de Columna | Tipo de Dato | Naturaleza | Según Estructura | Según Origen | Llave | Descripción |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id_cliente` | Entero | Cuantitativo | Estructurado | Primario | Primaria (PK) | Identificador numérico único para cada cliente. |
| `nombre_cliente` | Texto | Cualitativo | Estructurado | Primario | No aplica | Nombre y apellido del cliente. |
| `email` | Texto | Cualitativo | Estructurado | Primario | No aplica | Dirección de correo electrónico del cliente. |
| `ciudad` | Texto | Cualitativo | Estructurado | Primario | No aplica | Ciudad de residencia del cliente. |
| `fecha_alta` | Fecha | Cualitativo | Estructurado | Primario | No aplica | Fecha de registro del cliente en el sistema. |

---

### 2. Base de Datos: Productos
* **Fuente:** `productos.xlsx - productos.csv.csv`
* **Definición:** Catálogo maestro que describe cada uno de los productos disponibles para la venta.

| Nombre de Columna | Tipo de Dato | Naturaleza | Según Estructura | Según Origen | Llave | Descripción |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id_producto` | Entero | Cuantitativo | Estructurado | Primario | Primaria (PK) | Identificador numérico único para cada producto. |
| `nombre_producto` | Texto | Cualitativo | Estructurado | Primario | No aplica | Nombre comercial del producto. |
| `categoria` | Texto | Cualitativo | Estructurado | Primario | No aplica | Categoría a la que pertenece el producto (Alimentos, Limpieza). |
| `precio_unitario` | Decimal | Cuantitativo | Estructurado | Primario | No aplica | Precio de venta por una unidad del producto. |

---

### 3. Base de Datos: Ventas
* **Fuente:** `ventas.xlsx - ventas.csv.csv`
* **Definición:** Tabla transaccional que funciona como encabezado de cada orden de compra.

| Nombre de Columna | Tipo de Dato | Naturaleza | Según Estructura | Según Origen | Llave | Descripción |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id_venta` | Entero | Cuantitativo | Estructurado | Primario | Primaria (PK) | Identificador numérico único para cada transacción. |
| `fecha` | Fecha | Cualitativo | Estructurado | Primario | No aplica | Fecha en que se procesó la venta. |
| `id_cliente` | Entero | Cuantitativo | Estructurado | Primario | Foránea (FK) | Referencia al `id_cliente` en la tabla **Clientes**. |
| `nombre_cliente` | Texto | Cualitativo | Estructurado | Secundario | No aplica | Nombre del cliente (dato denormalizado para consulta rápida). |
| `email` | Texto | Cualitativo | Estructurado | Secundario | No aplica | Email del cliente (dato denormalizado para consulta rápida). |
| `medio_pago` | Texto | Cualitativo | Estructurado | Primario | No aplica | Método utilizado para el pago (tarjeta, qr, etc.). |

---

### 4. Base de Datos: Detalle de Ventas
* **Fuente:** `detalle_ventas.xlsx - detalle_ventas.csv.csv`
* **Definición:** Tabla transaccional que desglosa los productos y cantidades de cada venta.

| Nombre de Columna | Tipo de Dato | Naturaleza | Según Estructura | Según Origen | Llave | Descripción |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id_venta` | Entero | Cuantitativo | Estructurado | Primario | Foránea (FK) | Referencia al `id_venta` en la tabla **Ventas**. |
| `id_producto` | Entero | Cuantitativo | Estructurado | Primario | Foránea (FK) | Referencia al `id_producto` en la tabla **Productos**. |
| `nombre_producto` | Texto | Cualitativo | Estructurado | Secundario | No aplica | Nombre del producto (dato denormalizado). |
| `cantidad` | Entero | Cuantitativo | Estructurado | Primario | No aplica | Número de unidades vendidas del producto. |
| `precio_unitario` | Decimal | Cuantitativo | Estructurado | Secundario | No aplica | Precio del producto al momento de la venta (denormalizado). |
| `importe` | Decimal | Cuantitativo | Estructurado | Secundario | No aplica | Monto total por producto (`cantidad` * `precio_unitario`). |