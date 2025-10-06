'''
Este script de Python está diseñado para realizar un proceso completo de ETL (Extracción, Transformación y Carga) 
y análisis de datos de ventas de la empresa ficticia Aurelion.

Funcionalidades principales:
1.  **Carga de Datos:** Lee archivos de Excel desde una carpeta local que contienen información sobre clientes, 
    productos, ventas y detalles de ventas.
2.  **Limpieza de Datos:** Realiza operaciones de limpieza en cada conjunto de datos, como el manejo de valores nulos 
    y la corrección de tipos de datos para garantizar la calidad y consistencia de la información.
3.  **Unificación de Datos:** Combina los diferentes conjuntos de datos en un único DataFrame analítico. 
    Este DataFrame consolidado permite tener una visión integral del negocio, conectando ventas con clientes y productos.
4.  **Análisis Exploratorio (próximamente):** A partir del DataFrame unificado, se podrán realizar análisis para 
    extraer insights, como identificar los productos más vendidos, los clientes más valiosos, y las tendencias de ventas a lo largo del tiempo.

El código está estructurado de manera clara y comentado para facilitar su comprensión, especialmente para aquellos 
que se inician en el análisis de datos con Python y la librería pandas.
'''

import pandas as pd
import numpy as np
import os

# --- 1. Carga de Datos ---
# Define la ruta a la carpeta que contiene los archivos de Excel.
data_path = 'BDs'
clientes_path = os.path.join(data_path, 'clientes.xlsx')
productos_path = os.path.join(data_path, 'productos.xlsx')
ventas_path = os.path.join(data_path, 'ventas.xlsx')
detalle_ventas_path = os.path.join(data_path, 'detalle_ventas.xlsx')

# Cargar cada archivo de Excel en un DataFrame de pandas.
print("Cargando archivos...")
df_clientes = pd.read_excel(clientes_path)
df_productos = pd.read_excel(productos_path)
df_ventas = pd.read_excel(ventas_path)
df_detalle_ventas = pd.read_excel(detalle_ventas_path)
print("Archivos cargados correctamente.")

# --- 2. Limpieza y Preparación de Datos ---
print("\nIniciando limpieza de datos...")

# Limpieza de df_clientes
df_clientes['nombre_cliente'].fillna('Desconocido', inplace=True)
df_clientes['id_cliente'] = df_clientes['id_cliente'].astype(int)

# Limpieza de df_productos
df_productos['nombre_producto'].fillna('Sin Nombre', inplace=True)
df_productos['precio_unitario'] = pd.to_numeric(df_productos['precio_unitario'], errors='coerce')
df_productos['precio_unitario'].fillna(0, inplace=True)
df_productos['id_producto'] = df_productos['id_producto'].astype(int)

# Limpieza de df_ventas
df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
df_ventas['id_venta'] = df_ventas['id_venta'].astype(int)
df_ventas['id_cliente'] = df_ventas['id_cliente'].astype(int)

# Limpieza de df_detalle_ventas
df_detalle_ventas['id_venta'] = df_detalle_ventas['id_venta'].astype(int)
df_detalle_ventas['id_producto'] = df_detalle_ventas['id_producto'].astype(int)
df_detalle_ventas['cantidad'] = df_detalle_ventas['cantidad'].astype(int)

# Antes de unificar, eliminamos columnas duplicadas que ya existen en otras tablas
# para evitar conflictos en la unificación.
df_ventas.drop(columns=['nombre_cliente', 'email'], inplace=True)
df_detalle_ventas.drop(columns=['nombre_producto', 'precio_unitario', 'importe'], inplace=True)

print("Limpieza de datos completada.")

# --- 3. Unificación de Datos (Merge) ---
print("\nUnificando los datos en un único DataFrame...")

# Unimos ventas con los detalles de la venta
df_ventas_detalle = pd.merge(df_ventas, df_detalle_ventas, on='id_venta')

# Añadimos la información de los productos
df_ventas_productos = pd.merge(df_ventas_detalle, df_productos, on='id_producto')

# Finalmente, integramos la información de los clientes
df_analitico_principal = pd.merge(df_ventas_productos, df_clientes, on='id_cliente')

print("¡Unificación completada!")

# --- 4. Visualización del DataFrame Final ---
print("\nMostrando las primeras 10 filas del DataFrame analítico principal:")
print(df_analitico_principal.head(10))

print("\nInformación general del DataFrame final:")
df_analitico_principal.info()

# Guardar el DataFrame unificado en un nuevo archivo CSV o Excel.
output_path = os.path.join('BDSalida', 'reporte_analitico.csv')
df_analitico_principal.to_csv(output_path, index=False)
print(f"\nDataFrame analítico guardado como '{output_path}'")

# --- 5. Análisis de Datos ---
print("\n--- INICIANDO ANÁLISIS DE DATOS ---")

# Cargamos el dataset analítico que generamos en el paso anterior.
df_analisis = pd.read_csv(output_path)

# Calculamos la columna 'importe' que representa el valor total de cada línea de venta.
df_analisis['importe'] = df_analisis['cantidad'] * df_analisis['precio_unitario']

# 1) Top 5 Productos por Cantidad e Importe
print("\n--- 1. Top 5 Productos ---")
# Por cantidad
top_productos_cantidad = df_analisis.groupby('nombre_producto')['cantidad'].sum().nlargest(5)
print("\nTop 5 Productos por Cantidad Vendida:")
print(top_productos_cantidad)

# Por importe
top_productos_importe = df_analisis.groupby('nombre_producto')['importe'].sum().nlargest(5)
print("\nTop 5 Productos por Importe Total:")
print(top_productos_importe)

# 2) Top 5 Clientes por Gasto Acumulado
print("\n--- 2. Top 5 Clientes por Gasto ---")
top_clientes = df_analisis.groupby('nombre_cliente')['importe'].sum().nlargest(5)
print(top_clientes)

# 3) Ventas por Ciudad
print("\n--- 3. Ventas Totales por Ciudad ---")
ventas_ciudad = df_analisis.groupby('ciudad')['importe'].sum().sort_values(ascending=False)
print(ventas_ciudad)

# 4) Distribución de Medios de Pago
print("\n--- 4. Distribución de Medios de Pago ---")
distribucion_pago = df_analisis['medio_pago'].value_counts()
print(distribucion_pago)