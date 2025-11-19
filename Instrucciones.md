# INSTRUCCIONES GENERALES
Para ejecutar el programa por favor introducir en la terminal el comando `python Programa.py`

# INSTRUCCIONES SOLICITADAS A LA IA PARA SPRINT 1

## 1. Instrucciones para la Interfaz de Usuario (index.html)

1.  Implementa un saludo inicial en index.html al iniciar el chatbot que diga "¡Hola! Soy Aurelion, tu asistente virtual. ¿Sobre qué te gustaría saber?".
2.  Crea una lista de opciones en el menú desplegable (SELECT) del frontend con los siguientes 7 puntos documentados: "Tema del Proyecto", "Problema", "Solución Propuesta", "Set de datos", "Pasos", "Diagrama de flujo", y "Pseudocódigo".
3.  Implementa la librería marked.js en index.html para que las respuestas del bot (que vienen en formato Markdown) se rendericen correctamente como HTML.
4.  Si el servidor devuelve la bandera subsecciones: True, implementa en el frontend (index.html) la lógica para reemplazar el menú desplegable con botones de sub-opción.

## 2. Instrucciones para la Lógica del Servidor y Archivos (Programa.py)

1.  Crea una función (cargar_documentacion en Programa.py) que sea capaz de leer el archivo Documentación.md y dividir su contenido en secciones principales usando el patrón de título ##.
2.  Cuando el usuario selecciona la opción "4. Características set de datos", el backend debe detectar y devolver el mensaje introductorio de la sección 4, la bandera subsecciones: True y la lista de sub-opciones (4.1, 4.2, 4.3, 4.4).
3.  Implementar el manejo de peticiones POST que contengan la clave subopcion (por ejemplo, 4.1) para buscar y devolver el contenido específico del mapeo subsecciones_documentacion.

## 3. Instrucciones de Estructura y Estilo (CSS/HTML)

1.  Asegura que la ventana del chatbot (.chat-container) ocupe aproximadamente el 50% del ancho de la pantalla y que tenga un alto máximo de 700px.
2.  Diseña dos clases CSS (.bot-message y .user-message) con distintos colores de fondo (gris claro para el bot, azul para el usuario) y que se alineen a la izquierda y derecha de la ventana, respectivamente.

# INSTRUCCIONES SOLICITADAS A LA IA PARA SPRINT 2

## 1. Instrucciones para la Interfaz de Usuario (index.html)

1.  Agrega dos botones en la parte superior del `index.html`, uno para "SPRINT 1" y otro para "SPRINT 2", que permitan alternar entre las funcionalidades de cada sprint.
2.  Implementa la librería `marked.js` en `index.html` para que las respuestas del bot (que vienen en formato Markdown) se rendericen correctamente como HTML.
3.  Asegúrate de que al hacer clic en el botón "SPRINT 2", el menú de opciones se actualice con las nuevas funcionalidades correspondientes a este sprint.

## 2. Instrucciones para la Lógica del Servidor y Archivos (Programa.py)

1.  Modifica el menú de opciones en `Programa.py` para incluir las secciones del SPRINT 2.
2.  Implementa la lógica necesaria para que el backend devuelva las imágenes de los gráficos generados y se muestren en el chat del frontend.

## 3. Instrucciones de Estructura y Estilo (CSS/HTML)

1.  Asegúrate de que los botones "SPRINT 1" y "SPRINT 2" tengan un estilo claro y sean fácilmente accesibles para el usuario.
2.  Diseña un contenedor específico en el `index.html` donde se mostrarán los gráficos generados, asegurando que se visualicen correctamente.