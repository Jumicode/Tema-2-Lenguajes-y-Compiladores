// Definición de la clase Nodo
class Nodo {
    constructor(partida, cuerpo, firma_digital) {
        this.partida = partida;         // Hash de la partida anterior o inicial
        this.cuerpo = cuerpo;           // Arreglo de números aleatorios
        this.firma_digital = firma_digital; // Hash SHA-256 de la partida y el cuerpo
        this.siguiente = null;          // Referencia al siguiente nodo
    }
}

// Función asíncrona para calcular SHA-256 usando Web Crypto API
async function sha256(texto) {
    const encoder = new TextEncoder();
    // Crea un codificador de texto para convertir el string a bytes (UTF-8).

    const data = encoder.encode(texto);
    // Convierte el texto recibido en un arreglo de bytes.

    const hashBuffer = await crypto.subtle.digest("SHA-256", data);
    // Calcula el hash SHA-256 de los bytes usando la API Web Crypto, devuelve un ArrayBuffer.

    return [...new Uint8Array(hashBuffer)]
        // Convierte el ArrayBuffer a un arreglo de bytes (Uint8Array) y lo expande en un array normal.
        .map(b => b.toString(16).padStart(2, '0'))
        // Convierte cada byte a su representación hexadecimal de dos dígitos.
        .join('');
        // Une todos los bytes hexadecimales en un solo string y lo retorna.
}

// Función asíncrona para crear la lista enlazada
async function crearLista(n, k) {
    let cabeza = null;           // Inicializa la cabeza de la lista enlazada como null (vacía)
    let anterior = null;         // Inicializa la referencia al nodo anterior como null
    let partidaAnterior = "";    // Inicializa la partida anterior como cadena vacía

    for (let i = 0; i < n; i++) {   // Bucle para crear 'n' noos
        // Genera un arreglo de 'k' números aleatorios entre 1 y 100000 para el cuerpo del nodo
        const cuerpo = Array.from({ length: k }, () => Math.floor(Math.random() * 100000) + 1);

        if (i === 0) {  // Si es el primer nodo
            const timestamp = Date.now().toString();      // Obtiene el tiempo actual en milisegundos como string
            partidaAnterior = await sha256(timestamp);    // Calcula el hash SHA-256 del timestamp como partida inicial
        }

        // Une la partida anterior y los números del cuerpo en un solo string separados por espacios
        const datos = partidaAnterior + " " + cuerpo.join(" ");
        // Calcula el hash SHA-256 de ese string, que será la firma digital del nodo
        const firma = await sha256(datos);

        // Crea un nuevo nodo con la partida anterior, el cuerpo y la firma digital
        const nodo = new Nodo(partidaAnterior, cuerpo, firma);

        if (!cabeza) cabeza = nodo;           // Si es el primer nodo, lo asigna como cabeza de la lista
        if (anterior) anterior.siguiente = nodo; // Si no es el primero, enlaza el nodo anterior con el nuevo

        anterior = nodo;                      // Actualiza la referencia al nodo anterior para el siguiente ciclo
        partidaAnterior = firma;              // Actualiza la partida anterior con la firma actual para el siguiente nodo
    }

    return cabeza;                            // Devuelve la cabeza de la lista enlazada (primer nodo)
}

// Función para imprimir la lista enlazada
function imprimirLista(cabeza) {
    let actual = cabeza;            // Comienza desde la cabeza de la lista
    let index = 1;                  // Inicializa el contador de nodos
    while (actual) {                // Mientras el nodo actual no sea null
        console.log(`Nodo ${index}`); // Imprime el número del nodo
        console.log(` Partida: ${actual.partida}`);           // Imprime la partida (hash anterior)
        console.log(` Cuerpo: ${actual.cuerpo.join(" ")}`);   // Imprime el cuerpo (números aleatorios)
        console.log(` Firma: ${actual.firma_digital}`);       // Imprime la firma digital (hash SHA-256)
        console.log("---");          // Imprime un separador
        actual = actual.siguiente;   // Avanza al siguiente nodo
        index++;                     // Incrementa el contador
    }
}

// Función principal para ejecutar los escenarios y medir el tiempo
async function ejecutar() {
    const escenarios = [[3, 4], [10, 200], [200, 10]]; // Define los escenarios a probar
    for (const [n, k] of escenarios) {                 // Itera sobre cada escenario
        const inicio = performance.now();              // Guarda el tiempo inicial en milisegundos
        const lista = await crearLista(n, k);          // Crea la lista enlazada con n nodos y k elementos por nodo
        const fin = performance.now();                 // Guarda el tiempo final
        console.log(`Escenario (n=${n}, k=${k}) => ${Math.round(fin - inicio)} ms`); // Imprime el resultado
        // imprimirLista(lista);                       // (Opcional) Imprime la lista enlazada completa
    }
}

// Llama a la función principal
ejecutar();