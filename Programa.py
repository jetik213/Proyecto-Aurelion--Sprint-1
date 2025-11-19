# -*- coding: utf-8 -*-
import http.server
import socketserver
import json
import re
import os

PORT = 8000
DOC_FILE = os.path.join(os.path.dirname(__file__), 'Documentación.md')

def cargar_documentacion():
    contenido = {}
    subsecciones = {}
    try:
        with open(DOC_FILE, 'r', encoding='utf-8') as f:
            texto = f.read()

        # Dividir el texto en SPRINTs
        sprints = re.split(r'# (SPRINT \d+)', texto)
        
        # Procesar SPRINT 1
        sprint1_texto = sprints[2]
        secciones_s1 = re.split(r'\n## (\d\.\d+\. .*?)\n', sprint1_texto)
        for i in range(1, len(secciones_s1), 2):
            titulo = secciones_s1[i].strip()
            cuerpo = secciones_s1[i+1].strip()
            
            if titulo.startswith("1.4."):
                partes_subseccion = re.split(r'\n### (1\.4\.\d\..*?)\n', cuerpo)
                contenido[titulo] = partes_subseccion[0].strip()
                for j in range(1, len(partes_subseccion), 2):
                    sub_titulo = partes_subseccion[j].strip()
                    sub_cuerpo = partes_subseccion[j+1].strip().split('---\n---\n---')[0].strip()
                    subsecciones[sub_titulo] = sub_cuerpo
            else:
                contenido[titulo] = cuerpo.split('---\n---\n---')[0].strip()

        # Procesar SPRINT 2
        sprint2_texto = sprints[4]
        secciones_s2 = re.split(r'\n## (2\.\d+\.? .*?)\n', sprint2_texto)
        for i in range(1, len(secciones_s2), 2):
            titulo = secciones_s2[i].strip()
            cuerpo = secciones_s2[i+1].strip()

            if titulo.startswith("2.7"):
                partes_subseccion = re.split(r'\n?### (2\.7\.\d .*?)\n', cuerpo)
                contenido[titulo] = partes_subseccion[0].strip()
                for j in range(1, len(partes_subseccion), 2):
                    sub_titulo = partes_subseccion[j].strip()
                    sub_cuerpo = partes_subseccion[j+1].strip().split('---\n---\n---')[0].strip()
                    subsecciones[sub_titulo] = sub_cuerpo
            else:
                contenido[titulo] = cuerpo.split('---\n---\n---')[0].strip()

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {DOC_FILE}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        
    return contenido, subsecciones

documentacion, subsecciones_documentacion = cargar_documentacion()

mapeo_menu = {
    "1.1": "1.1. Tema del Proyecto",
    "1.2": "1.2. Problema",
    "1.3": "1.3. Solución Propuesta",
    "1.4": "1.4. Características set de datos",
    "1.5": "1.5. Pasos",
    "1.6": "1.6. Diagrama de flujo",
    "1.7": "1.7. Pseudocódigo",
    "2.1": "2.1. Problema",
    "2.2": "2.2. Solución Propuesta",
    "2.3": "2.3 Limpieza de Datos",
    "2.4": "2.4. Estadísticas descriptivas básicas calculadas",
    "2.5": "2.5. Identificación de Tipo de Distribución de variables",
    "2.6": "2.6. Detección de Outliers (Cuartiles y Rangos)",
    "2.7": "2.7 Gráficos",
    "2.8": "2.8 Interpretación de resultados"
}

mapeo_subsecciones = {
    "1.4.1": "1.4.1. Base de Datos: Clientes",
    "1.4.2": "1.4.2. Base de Datos: Productos",
    "1.4.3": "1.4.3. Base de Datos: Ventas",
    "1.4.4": "1.4.4. Base de Datos: Detalle de Ventas",
    "2.7.1": "2.7.1 Análisis de Pareto (80/20)",
    "2.7.2": "2.7.2 Análisis de Demanda Geoespacial",
    "2.7.3": "2.7.3 Análisis de Tendencia Temporal"
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
                elif opcion == "1.4":
                    intro_seccion = documentacion.get(mapeo_menu.get("1.4"), "")
                    response_data = {
                        'respuesta': intro_seccion,
                        'subsecciones': True,
                        'opciones_subseccion': [
                            { "texto": "Base de Datos: Clientes", "valor": "1.4.1" },
                            { "texto": "Base de Datos: Productos", "valor": "1.4.2" },
                            { "texto": "Base de Datos: Ventas", "valor": "1.4.3" },
                            { "texto": "Base de Datos: Detalle de Ventas", "valor": "1.4.4" }
                        ]
                    }
                elif opcion == "2.7":
                    intro_seccion = documentacion.get(mapeo_menu.get("2.7"), "")
                    response_data = {
                        'respuesta': intro_seccion,
                        'subsecciones': True,
                        'opciones_subseccion': [
                            { "texto": "Análisis de Pareto (80/20)", "valor": "2.7.1" },
                            { "texto": "Análisis de Demanda Geoespacial", "valor": "2.7.2" },
                            { "texto": "Análisis de Tendencia Temporal", "valor": "2.7.3" }
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

    def do_GET(self):
        if self.path == '/':
            self.path = '/templates/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), ChatbotHandler) as httpd:
    print("¡Hola! Soy Aurelion, tu asistente virtual.")
    print(f"Puedes hablar conmigo abriendo tu navegador y visitando: http://localhost:{PORT}")
    print(f"Si ya me usaste antes y quieres ver mi nueva versión, limpia la caché de tu navegador o ábreme en modo incógnito por favor!")
    httpd.serve_forever()
