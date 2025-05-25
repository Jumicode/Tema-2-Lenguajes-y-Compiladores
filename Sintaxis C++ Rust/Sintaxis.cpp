#include <iostream>  // librería estándar para entrada/salida

// Definición de una clase genérica usando template
template<typename T>
class Contador {
public:
    Contador(T inicio) : valor(inicio) {}  // constructor (identificador valor)
    
    void incrementar() {  // palabra clave, identificador, delimitadores
        valor = valor + 1;  // operador +, asignación
    }
    
    T obtener() const {  // literal de tipo bool en retorno (no aquí)
        return valor;  // palabra clave return, identificador valor
    }

private:
    T valor;  // identificador, delimitador ;
};

int main() {  // palabra clave int, identificador main, delimitadores ()
    // Literales: entero 0, flotante 3.14, cadena "Hola"
    int contadorEntero = 0;                    // literal entero, identificador, delimitador ;
    double pi = 3.14;                          // literal flotante, identificador
    std::string saludo = "Hola, C++!";       // literal cadena
    bool bandera = true;                       // literal booleano true

    // Mostrar saludo
    std::cout << saludo << std::endl;  // operador <<, delimitador ;

    // Estructura de control if-else
    if (bandera) {                       // palabra clave if, delimitadores ()
        std::cout << "Bandera es verdadera" << std::endl;
    } else {                            // palabra clave else
        std::cout << "Bandera es falsa" << std::endl;
    }

    // Ciclo while
    while (contadorEntero < 5) {        // palabra clave while, operador <
        std::cout << "Contador: " << contadorEntero << std::endl;
        contadorEntero++;                // operador ++
    }

    // Usar la clase templada Contador
    Contador<int> miContador(10);       // template, literal entero
    miContador.incrementar();           // llamada a método
    std::cout << "Valor de miContador: " << miContador.obtener() << std::endl;

    return 0;  // palabra clave return, literal entero
    }