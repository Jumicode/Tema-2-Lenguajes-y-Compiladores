import hashlib           # Importa la librería para funciones hash (SHA-256)
import random            # Importa la librería para generar números aleatorios
import time              # Importa la librería para trabajar con tiempo
from datetime import datetime  # (No se usa en el código, pero permite trabajar con fechas y horas)

class Nodo:
    def __init__(self, partida, cuerpo, firma_digital):
        self.partida = partida           # Guarda el hash de la partida anterior o inicial
        self.cuerpo = cuerpo             # Guarda la lista de números aleatorios
        self.firma_digital = firma_digital # Guarda el hash SHA-256 de la partida y el cuerpo
        self.siguiente = None            # Referencia al siguiente nodo (inicia en None)

def calcular_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()  # Codifica el texto y calcula el hash SHA-256

def crear_lista_enlazada(n, k):
    cabeza = None                  # Referencia al primer nodo de la lista
    nodo_anterior = None           # Referencia al nodo anterior (para enlazar)
    partida_anterior = ""          # Guarda el hash de la partida anterior

    for i in range(n):             # Repite n veces para crear n nodos
        cuerpo = [random.randint(1, 100000) for _ in range(k)]  # Genera k números aleatorios

        if not partida_anterior:                   # Si es el primer nodo
            ahora = int(time.time())               # Obtiene el tiempo actual en segundos
            partida_anterior = calcular_sha256(str(ahora)) # Calcula el hash del tiempo como partida inicial

        texto_a_hashear = partida_anterior + ' ' + ' '.join(map(str, cuerpo)) # Une la partida y el cuerpo en un string
        firma = calcular_sha256(texto_a_hashear)   # Calcula el hash SHA-256 de ese string

        nuevo_nodo = Nodo(partida_anterior, cuerpo, firma)  # Crea el nodo con los datos calculados
        if cabeza is None:                        # Si es el primer nodo
            cabeza = nuevo_nodo                   # Lo asigna como cabeza de la lista
        else:
            nodo_anterior.siguiente = nuevo_nodo  # Si no, enlaza el nodo anterior con el nuevo

        nodo_anterior = nuevo_nodo                # Actualiza el nodo anterior
        partida_anterior = firma                  # Actualiza la partida para el siguiente nodo

    return cabeza                                 # Devuelve la cabeza de la lista enlazada

def imprimir_lista(cabeza):
    nodo = cabeza                  # Comienza desde la cabeza de la lista
    contador = 1                   # Inicializa el contador de nodos
    while nodo:                    # Mientras el nodo actual no sea None
        print(f"Nodo {contador}:") # Imprime el número del nodo
        print(f" Partida: {nodo.partida}")           # Imprime la partida (hash anterior)
        print(f" Cuerpo: {' '.join(map(str, nodo.cuerpo))}") # Imprime el cuerpo (números aleatorios)
        print(f" Firma Digital: {nodo.firma_digital}")       # Imprime la firma digital (hash SHA-256)
        print("---")                 # Imprime un separador
        nodo = nodo.siguiente        # Avanza al siguiente nodo
        contador += 1                # Incrementa el contador

def medir_tiempo(n, k):
    inicio = time.time()             # Guarda el tiempo inicial en segundos
    cabeza = crear_lista_enlazada(n, k) # Crea la lista enlazada con n nodos y k elementos por nodo
    fin = time.time()                # Guarda el tiempo final en segundos
    duracion_ms = (fin - inicio) * 1000 # Calcula la duración en milisegundos
    print(f"Escenario (n={n}, k={k}) => {duracion_ms:.2f} ms") # Imprime el resultado
    # imprimir_lista(cabeza)         # (Opcional) Imprime la lista enlazada completa

# Ejecutar los tres escenarios
escenarios = [(3, 4), (10, 200), (200, 10)]  # Lista de escenarios (nodos, elementos por nodo)
for n, k in escenarios:
    medir_tiempo(n, k)                      # Ejecuta la medición para cada escenario