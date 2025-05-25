// Estructura genérica usando traits y genéricos
struct Contador<T> {
    valor: T,  // identificador 'valor'
}

impl<T> Contador<T>
where
    T: std::ops::Add<Output = T> + Copy,
{
    // constructor equivalente
    fn new(inicio: T) -> Contador<T> {
        Contador { valor: inicio }  // palabra clave 'new', identificadores, delimitador '{}'
    }

    fn incrementar(&mut self) {
        // operador '+' y asignación
        self.valor = self.valor + T::from(1u8); // literal entero '1', conversión
    }

    fn obtener(&self) -> T {
        self.valor  // palabra clave 'return' implícita en Rust
    }
}

fn main() {
    // Literales: entero, flotante, caracter, cadena, booleano
    let mut contador_entero: i32 = 0;        // keyword 'let mut', identificador, tipo i32
    let pi: f64 = 3.14;                     // literal flotante
    let caracter: char = 'a';               // literal caracter
    let saludo: &str = "Hola, Rust!";      // literal cadena
    let bandera: bool = true;               // literal booleano

    // Mostrar saludo
    println!("{}", saludo);               // macro println!, delimitadores '()' y format string

    // Estructura if-else
    if bandera && contador_entero == 0 {    // operadores '&&', '=='
        println!("Bandera es verdadera y contador es cero");
    } else {
        println!("Condición no cumplida");
    }

    // Ciclo while
    while contador_entero < 5 {             // operador '<'
        println!("Contador: {}", contador_entero);
        contador_entero += 1;               // operador '+='
    }

    // Usar la estructura genérica Contador
    let mut mi_contador = Contador::new(10);  // llamada a función asociada, literal entero
    mi_contador.incrementar();                // método incrementar
    println!("Valor de mi_contador: {}", mi_contador.obtener());

    // Comentario de bloque
    /*
       Este es un comentario de
       múltiples líneas en Rust.
    */
}