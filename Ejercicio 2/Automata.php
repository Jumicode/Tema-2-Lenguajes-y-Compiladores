<?php

// Definición de la clase Nodo
class Nodo {
    public $partida;         // Hash de la partida anterior o inicial
    public $cuerpo;          // Arreglo de números aleatorios
    public $firma_digital;   // Hash SHA-256 de la partida y el cuerpo
    public $siguiente;       // Referencia al siguiente nodo

    // Constructor del nodo
    public function __construct($partida, $cuerpo, $firma_digital) {
        $this->partida = $partida;
        $this->cuerpo = $cuerpo;
        $this->firma_digital = $firma_digital;
        $this->siguiente = null;
    }
}

// Función para calcular el hash SHA-256 de un texto
function calcular_sha256($texto) {
    return hash("sha256", $texto);
}

// Función para crear una lista enlazada de n nodos, cada uno con k números aleatorios
function crear_lista($n, $k) {
    $cabeza = null;                // Inicializa la cabeza de la lista enlazada como null (vacía)
    $anterior = null;              // Inicializa la referencia al nodo anterior como null
    $partida_anterior = "";        // Inicializa la partida anterior como cadena vacía

    for ($i = 0; $i < $n; $i++) {  // Bucle para crear 'n' nodos
        $cuerpo = [];              // Inicializa el arreglo que contendrá los números aleatorios
        for ($j = 0; $j < $k; $j++) {
            $cuerpo[] = rand(1, 100000); // Genera un número aleatorio entre 1 y 100000 y lo agrega al cuerpo
        }

        if ($i === 0) {            // Si es el primer nodo
            $partida_anterior = calcular_sha256(time()); // Calcula el hash SHA-256 del tiempo actual como partida inicial
        }

        $texto_a_hashear = $partida_anterior . ' ' . implode(' ', $cuerpo);
        // Une la partida anterior y los números del cuerpo en un solo string separados por espacios

        $firma_digital = calcular_sha256($texto_a_hashear);
        // Calcula el hash SHA-256 de ese string, que será la firma digital del nodo

        $nuevo_nodo = new Nodo($partida_anterior, $cuerpo, $firma_digital);
        // Crea un nuevo nodo con la partida anterior, el cuerpo y la firma digital

        if ($cabeza === null) {    // Si es el primer nodo de la lista
            $cabeza = $nuevo_nodo; // Lo asigna como cabeza de la lista
        } else {
            $anterior->siguiente = $nuevo_nodo;
            // Si no es el primero, enlaza el nodo anterior con el nuevo
        }

        $anterior = $nuevo_nodo;   // Actualiza la referencia al nodo anterior para el siguiente ciclo
        $partida_anterior = $firma_digital; // Actualiza la partida anterior con la firma actual para el siguiente nodo
    }

    return $cabeza;                // Devuelve la cabeza de la lista enlazada (primer nodo)
}

// Función para imprimir la lista enlazada
function imprimir_lista($cabeza) {
    $nodo = $cabeza;                // Comienza desde la cabeza de la lista
    $indice = 1;                    // Inicializa el contador de nodos
    while ($nodo !== null) {        // Mientras el nodo actual no sea null
        echo "Nodo $indice:\n";     // Imprime el número del nodo
        echo " Partida: {$nodo->partida}\n";           // Imprime la partida (hash anterior)
        echo " Cuerpo: " . implode(' ', $nodo->cuerpo) . "\n"; // Imprime el cuerpo (números aleatorios)
        echo " Firma Digital: {$nodo->firma_digital}\n";       // Imprime la firma digital (hash SHA-256)
        echo "---\n";               // Imprime un separador
        $nodo = $nodo->siguiente;   // Avanza al siguiente nodo
        $indice++;                  // Incrementa el contador
    }
}

// Función para ejecutar los escenarios de prueba y medir el tiempo
function ejecutar_escenarios() {
    $escenarios = [[3, 4], [10, 200], [200, 10]]; // Define los escenarios a probar
    foreach ($escenarios as [$n, $k]) {           // Itera sobre cada escenario
        $inicio = microtime(true);                // Guarda el tiempo inicial en segundos (con microsegundos)
        $cabeza = crear_lista($n, $k);            // Crea la lista enlazada con n nodos y k elementos por nodo
        $fin = microtime(true);                   // Guarda el tiempo final
        $duracion = ($fin - $inicio) * 1000;      // Calcula la duración en milisegundos
        echo "Escenario (n=$n, k=$k) => " . number_format($duracion, 2) . " ms\n"; // Imprime el resultado
        // imprimir_lista($cabeza);               // (Opcional) Imprime la lista enlazada completa
    }
}

// Llama a la función principal
ejecutar_escenarios();