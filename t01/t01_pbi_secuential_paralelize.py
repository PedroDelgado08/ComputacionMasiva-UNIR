# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 12:44:24 2025

@author: carlo
"""

import time
import csv
from concurrent.futures import ThreadPoolExecutor

# Configuración
num_operaciones = 300
tiempo_por_operacion = 0.1  # segundos
archivo_secuencial = 'secuencial.csv'
archivo_paralelo_3 = 'paralelo_3hilos.csv'
archivo_paralelo_4 = 'paralelo_4hilos.csv'
archivo_paralelo_6 = 'paralelo_6hilos.csv'

# Función que simula una operación
def operacion():
    time.sleep(tiempo_por_operacion)
    return 1

# --- Ejecución secuencial ---
resultados_secuencial = []
inicio = time.time()
for i in range(1, num_operaciones + 1):
    operacion()
    t = time.time() - inicio
    resultados_secuencial.append((t, i))

with open(archivo_secuencial, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Tiempo(s)', 'Operaciones_completadas'])
    for t, c in resultados_secuencial:
        writer.writerow([f"{t:.6f}", c])

# --- Función para ejecución paralela ---
def ejecutar_paralelo(num_hilos, archivo_salida):
    resultados = []
    inicio = time.time()
    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        futures = [executor.submit(operacion) for _ in range(num_operaciones)]
        completadas = 0
        for future in futures:
            future.result()
            completadas += 1
            t = time.time() - inicio
            resultados.append((t, completadas))
    # Guardar CSV
    with open(archivo_salida, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Tiempo(s)', 'Operaciones_completadas'])
        for t, c in resultados:
            writer.writerow([f"{t:.6f}", c])
    print(f"Paralelo {num_hilos} hilos completado. CSV generado: {archivo_salida}")

# --- Ejecuciones paralelas ---
ejecutar_paralelo(3, archivo_paralelo_3)
ejecutar_paralelo(4, archivo_paralelo_4)
ejecutar_paralelo(6, archivo_paralelo_6)

print("Simulación completa para secuencial y paralelos.")
