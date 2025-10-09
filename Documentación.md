# DOCUMENTACIÓN.md

## 1. Tema del Proyecto
**"Chatbot Interactivo para el Minimarket Aurelion"**  
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

* **Nota: Todos los campos provienen de origen **Primario** y tienen una estructura de forma **Estructurada**.**
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

* **Nota: Todos los campos provienen de origen **Primario** y tienen una estructura de forma **Estructurada**.**
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

* **Nota: Todos los campos provienen de origen **Primario** y tienen una estructura de forma **Estructurada**.**
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

* **Nota: Todos los campos provienen de origen **Primario** y tienen una estructura de forma **Estructurada**.**
---

## 5. Pasos
### Paso 1: Configuración y Variables Globales ⚙️
En este primer paso, se prepara todo lo necesario para que el programa funcione. Se definen **parámetros fijos** como el puerto `8000` donde operará el servidor y la ubicación del archivo `Documentación.md`. Además, se crean "contenedores" o **diccionarios vacíos** que más adelante guardarán la información leída del documento. Finalmente, se establecen "mapas" que traducen las opciones del usuario (como "1" o "4.1") a los títulos reales de las secciones en el documento.


### Paso 2: Función para Cargar y Procesar el Documento 📄➡️🧠
Este es el cerebro del programa. Aquí se define una función que **lee el archivo `Documentación.md` y lo procesa**. La función abre el archivo, lo divide inteligentemente en secciones principales (usando `##`) y subsecciones (usando `###`), y limpia cada trozo de texto. Toda esta información ya organizada se guarda en los diccionarios que se crearon en el paso anterior, dejando los datos listos para ser consultados.


### Paso 3: Ejecución Principal y Lógica del Servidor 🌐💬
En el último paso, el programa se pone en marcha. Primero, llama a la función del paso 2 para cargar toda la documentación en memoria. Luego, **inicia un servidor web** que se queda a la espera de que un usuario se conecte. El servidor sabe cómo manejar dos tipos de peticiones:
* Si es una petición **GET** (cuando el usuario entra a la página por primera vez), le sirve la interfaz gráfica (el archivo `index.html`).
* Si es una petición **POST** (cuando el usuario hace clic en una opción del chatbot), el servidor analiza la opción elegida, busca la respuesta correspondiente en los datos ya cargados y se la devuelve al navegador para que la muestre.
---

## 6. Diagrama de flujo
Para ver el Diagrama de Flujo da click en el siguiente enlace:  
<a href="https://drive.google.com/file/d/14wclspP4Igc2m6Fjd_yUgE8aAijw5vF-/view?usp=sharing" target="_blank">Diagrama de Flujo</a>
---

## 7. Pseudocódigo
### Paso 1: Configuración y Variables Globales
```plaintext
// Definir constantes y variables que se usarán en todo el programa.
CONSTANTE PUERTO = 8000
CONSTANTE RUTA_DOCUMENTO = "ruta/a/Documentación.md"

// Declarar variables para almacenar el contenido procesado del documento.
VARIABLE GLOBAL documentacion = DICCIONARIO VACÍO
VARIABLE GLOBAL subsecciones_documentacion = DICCIONARIO VACÍO

// Mapear las opciones del menú a los títulos exactos de las secciones en el documento.
CONSTANTE mapeo_menu = {
    "1": "1. Tema del Proyecto",
    "2": "2. Problema",
    "3": "3. Solución Propuesta",
    "4": "4. Características set de datos",
    "5": "5. Pasos",
    "6": "6. Diagrama de flujo",
    "7": "7. Pseudocódigo"
}

// Mapear las opciones del submenú a los títulos de las subsecciones.
CONSTANTE mapeo_subsecciones = {
    "4.1": "4.1. Base de Datos: Clientes",
    "4.2": "4.2. Base de Datos: Productos",
    "4.3": "4.3. Base de Datos: Ventas",
    "4.4": "4.4. Base de Datos: Detalle de Ventas"
}
```

### Paso 2: Función para Cargar y Procesar el Documento
```plaintext
FUNCIÓN cargar_documentacion():
    // Esta función lee el archivo .md y lo divide en secciones y subsecciones.
    
    // Inicializar diccionarios para guardar el contenido.
    VARIABLE contenido_local = DICCIONARIO VACÍO
    VARIABLE subsecciones_locales = DICCIONARIO VACÍO

    // Intentar leer el archivo para manejar posibles errores.
    INTENTAR:
        // Abrir y leer todo el texto del archivo.
        VARIABLE texto_completo = LEER_ARCHIVO(RUTA_DOCUMENTO)
        
        // Dividir el texto en partes usando los títulos de sección (##) como separadores.
        VARIABLE secciones = DIVIDIR_TEXTO(texto_completo, usando el patrón de título "## \d. ...")

        // Recorrer la lista de secciones para procesar cada título y su contenido.
        PARA cada i DESDE 1 HASTA LONGITUD(secciones) CON PASO 2:
            VARIABLE titulo = secciones[i]
            VARIABLE cuerpo = secciones[i+1]

            // Caso especial para la sección "4. Características set de datos".
            SI titulo ES IGUAL A "4. Características set de datos":
                VARIABLE partes_subseccion = DIVIDIR_TEXTO(cuerpo, usando el patrón de subtítulo "### 4.\d. ...")
                contenido_local[titulo] = partes_subseccion[0]

                // Recorrer las subsecciones para guardarlas.
                PARA cada j DESDE 1 HASTA LONGITUD(partes_subseccion) CON PASO 2:
                    VARIABLE sub_titulo = partes_subseccion[j]
                    VARIABLE sub_cuerpo = partes_subseccion[j+1]
                    subsecciones_locales[sub_titulo] = OBTENER_TEXTO_ANTES_DE(sub_cuerpo, "- - -")
                FIN PARA
            SINO:
                // Para todas las demás secciones.
                contenido_local[titulo] = OBTENER_TEXTO_ANTES_DE(cuerpo, "- - -")
            FIN SI
        FIN PARA
        
    CAPTURAR FileNotFoundError:
        ESCRIBIR_EN_CONSOLA("Error: No se encontró el archivo de documentación.")
    CAPTURAR OtroError:
        ESCRIBIR_EN_CONSOLA("Error al leer el archivo.")
    
    // Devolver los diccionarios con la información.
    RETORNAR contenido_local, subsecciones_locales
FIN FUNCIÓN
```

### Paso 3: Ejecución Principal y Lógica del Servidor
```plaintext
// Llamar a la función al iniciar el programa.
documentacion, subsecciones_documentacion = cargar_documentacion()

// Iniciar el servidor web.
INICIAR SERVIDOR en PUERTO con el manejador de peticiones:
    
    ESCRIBIR_EN_CONSOLA("¡Hola! Soy Aurelion, tu asistente virtual.")
    ESCRIBIR_EN_CONSOLA("Servidor iniciado en http://localhost:" + PUERTO)

    // El servidor se queda esperando peticiones.
    MIENTRAS SERVIDOR_ESTE_ACTIVO:
        ESPERAR_PETICION()

                // *** MANEJADOR DE PETICIONES ***
        
        // CUANDO LLEGA UNA PETICIÓN GET:
        PROCEDIMIENTO manejar_peticion_GET(peticion):
            SI peticion.ruta ES IGUAL A "/":
                peticion.ruta = "/templates/index.html"
            FIN SI
            SERVIR_ARCHIVO(peticion.ruta)
        FIN PROCEDIMIENTO

        // CUANDO LLEGA UNA PETICIÓN POST a /api/chatbot:
        PROCEDIMIENTO manejar_peticion_POST(peticion):
            SI peticion.ruta ES IGUAL A "/api/chatbot":
                INTENTAR:
                    VARIABLE datos_recibidos = LEER_CUERPO_JSON(peticion)
                    VARIABLE opcion_usuario = datos_recibidos["opcion"]
                    VARIABLE subopcion_usuario = datos_recibidos["subopcion"]
                    VARIABLE datos_respuesta = DICCIONARIO VACÍO

                    // Lógica para decidir qué responder.
                    SI subopcion_usuario EXISTE:
                        VARIABLE titulo_sub = mapeo_subsecciones[subopcion_usuario]
                        datos_respuesta["respuesta"] = subsecciones_documentacion[titulo_sub]
                    
                    SINO SI opcion_usuario ES IGUAL A "4":
                        VARIABLE titulo_seccion = mapeo_menu["4"]
                        datos_respuesta["respuesta"] = documentacion[titulo_seccion]
                        datos_respuesta["subsecciones"] = VERDADERO
                        datos_respuesta["opciones_subseccion"] = [
                            { "texto": "Base de Datos: Clientes", "valor": "4.1" },
                            // ... y las otras subopciones ...
                        ]

                    SINO SI opcion_usuario EXISTE:
                        VARIABLE titulo_seccion = mapeo_menu[opcion_usuario]
                        datos_respuesta["respuesta"] = documentacion[titulo_seccion]
                    
                    SINO:
                        ENVIAR_RESPUESTA_ERROR(400, "Opción no válida.")
                        RETORNAR
                    FIN SI

                    ENVIAR_RESPUESTA_OK(200, datos_respuesta)

                CAPTURAR ErrorDeServidor:
                    ENVIAR_RESPUESTA_ERROR(500, "Error interno del servidor.")
                FIN INTENTAR
            FIN SI
        FIN PROCEDIMIENTO
    FIN MIENTRAS
```
---

## 8. Ejecutar programa
Para ejecutar el programa por favor introducir en la terminal el comando `python Programa.py`