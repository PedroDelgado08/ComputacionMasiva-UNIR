# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 17:19:44 2025

@author: carlo
"""




import time
from concurrent.futures import ProcessPoolExecutor

# Función "pesada": simula un cálculo costoso (por ejemplo, verificar números primos)
def tarea_pesada(n):
    print(f"Iniciando tarea {n}")
    total = 0
    for i in range(10000000):
        total += (i * i) % 7
    print(f"Terminó tarea {n}")
    return total


if __name__ == '__main__':
	numeros = [1, 2, 3, 4]  # Cuatro tareas
	print("=== Ejecución secuencial ===")
	inicio = time.time()
	resultados_seq = [tarea_pesada(n) for n in numeros]
	fin = time.time()
	print(f"Tiempo secuencial: {fin - inicio:.2f} segundos\n")
	print("=== Ejecución en paralelo ===")
	inicio = time.time()
	with ProcessPoolExecutor() as executor:
          resultados_par = list(executor.map(tarea_pesada, numeros))
	
	fin = time.time()
	print(f"Tiempo en paralelo: {fin - inicio:.2f} segundos\n")

	print("Resultados iguales:", resultados_seq == resultados_par)