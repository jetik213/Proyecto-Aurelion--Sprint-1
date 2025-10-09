# -*- coding: utf-8 -*-
# Importamos los módulos necesarios de la biblioteca estándar de Python.
# http.server nos permite crear un servidor web.
# socketserver nos ayuda a manejar las conexiones de red.
# json nos permite trabajar con datos en formato JSON.
# re nos permite trabajar con expresiones regulares para buscar texto.
import http.server
import socketserver
import json
import re
import os

# Definimos el puerto en el que nuestro servidor escuchará las solicitudes.
PORT = 8000

# Definimos la ruta al archivo de documentación.
# os.path.join se usa para crear una ruta de archivo que funcione en cualquier sistema operativo.
DOC_FILE = os.path.join(os.path.dirname(__file__), 'Documentación.md')

# Función para leer y procesar el archivo de documentación.
def cargar_documentacion():
    contenido = {}
    subsecciones_4 = {}
    try:
        with open(DOC_FILE, 'r', encoding='utf-8') as f:
            texto = f.read()
        
        secciones = re.split(r'\n## (\d+\.\s.*?)\n', texto)
        
        for i in range(1, len(secciones), 2):
            titulo = secciones[i].strip()
            cuerpo = secciones[i+1].strip()
            
            if titulo == "4. Características set de datos":
                partes_subseccion = re.split(r'\n### (4\.\d\..*?)\n', cuerpo)
                contenido[titulo] = partes_subseccion[0].strip()
                
                for j in range(1, len(partes_subseccion), 2):
                    sub_titulo = partes_subseccion[j].strip()
                    sub_cuerpo = partes_subseccion[j+1].strip().split('---')[0].strip()
                    subsecciones_4[sub_titulo] = sub_cuerpo
            else:
                contenido[titulo] = cuerpo.split('---')[0].strip()
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {DOC_FILE}")
        return {}, {}
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return {}, {}
        
    return contenido, subsecciones_4

documentacion, subsecciones_documentacion = cargar_documentacion()

# Mapeamos los números del menú a los títulos de las secciones.
mapeo_menu = {
    "1": "1. Tema del Proyecto",
    "2": "2. Problema",
    "3": "3. Solución Propuesta",
    "4": "4. Características set de datos",
    "5": "5. Pasos",
    "6": "6. Diagrama de flujo",
    "7": "7. Pseudocódigo"
}

# Mapeo para las subsecciones de la opción 4.
mapeo_subsecciones = {
    "4.1": "4.1. Base de Datos: Clientes",
    "4.2": "4.2. Base de Datos: Productos",
    "4.3": "4.3. Base de Datos: Ventas",
    "4.4": "4.4. Base de Datos: Detalle de Ventas"
}

class ChatbotHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/chatbot':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                body = json.loads(post_data)
                opcion = body.get('opcion')
                subopcion = body.get('subopcion')

                response_data = {}

                if subopcion:
                    titulo_subseccion = mapeo_subsecciones.get(subopcion)
                    respuesta = subsecciones_documentacion.get(titulo_subseccion, "Información no disponible.")
                    response_data = {'respuesta': respuesta}
                elif opcion == "4":
                    intro_seccion_4 = documentacion.get(mapeo_menu.get("4"), "")
                    response_data = {
                        'respuesta': intro_seccion_4,
                        'subsecciones': True,
                        'opciones_subseccion': [
                            { "texto": "Base de Datos: Clientes", "valor": "4.1" },
                            { "texto": "Base de Datos: Productos", "valor": "4.2" },
                            { "texto": "Base de Datos: Ventas", "valor": "4.3" },
                            { "texto": "Base de Datos: Detalle de Ventas", "valor": "4.4" }
                        ]
                    }
                elif opcion:
                    titulo_seccion = mapeo_menu.get(opcion)
                    respuesta = documentacion.get(titulo_seccion, "Información no disponible.")
                    if not respuesta.strip():
                        respuesta = "Esta sección no tiene contenido en el archivo de documentación."
                    response_data = {'respuesta': respuesta}
                else:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'No se especificó una opción válida.'}).encode('utf-8'))
                    return

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        else:
            super().do_POST()

    # Este método se ejecuta cuando llega una solicitud GET.
    def do_GET(self):
        # Si el usuario pide la página principal, le servimos el archivo index.html.
        if self.path == '/':
            # Cambiamos la ruta para que apunte al archivo dentro de la carpeta 'templates'.
            self.path = '/templates/index.html'
        # Dejamos que la clase base maneje la solicitud para servir el archivo.
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Configuramos el servidor para que use nuestro manejador de solicitudes.
with socketserver.TCPServer(("", PORT), ChatbotHandler) as httpd:
    print("¡Hola! Soy Aurelion, tu asistente virtual.")
    print(f"Puedes hablar conmigo abriendo tu navegador y visitando: http://localhost:{PORT}")
    # Ponemos el servidor en marcha para que empiece a escuchar solicitudes.
    httpd.serve_forever()
