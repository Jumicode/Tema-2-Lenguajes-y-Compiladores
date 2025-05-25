# ------------------------------
# Descripción del Problema
# ------------------------------
# Un usuario interactúa con una máquina dispensadora de golosinas a través de una pantalla o consola.
# La máquina ofrece los siguientes productos:
#
# - Chocolates (5 $)
# - Caramelos  (2 $)
# - Chicles    (3 $)
# - Chupetas   (6 $)
#
# Flujo de operación:
# 1. El usuario selecciona el producto deseado.
# 2. Introduce el dinero correspondiente.
# 3. La máquina realiza las siguientes acciones:
#    - Verifica si el monto ingresado es suficiente.
#    - Si es suficiente, entrega el producto en un tiempo estimado de 5 segundos.
#    - Si sobra dinero, devuelve el cambio en 8 segundos.

import os
from time import sleep

def verificacion_golosina(golosina_seleccionada, monto_ingresado):
    if golosina_seleccionada == 1 and monto_ingresado >= 5:
        print("Aquí tienes tu chocolate 🍫")
        monto_ingresado -= 5

    elif golosina_seleccionada == 2 and monto_ingresado >= 2:
        print("Aquí tienes tus caramelos 🍬")
        monto_ingresado -= 2

    elif golosina_seleccionada == 3 and monto_ingresado >= 3:
        print("Aquí tienes tus chicles 🍥")
        monto_ingresado -= 3

    elif golosina_seleccionada == 4 and monto_ingresado >= 6:
        print("Aquí tienes tu chupeta 🍭")
        monto_ingresado -= 6

    else:
        if monto_ingresado == 0:
            print("No has ingresado nada...")
        else:
            print("No tienes suficiente dinero para comprar esa golosina")
        
        input("Presiona Enter para continuar...")   
        return False

    print("Tu compra ha sido procesada con exito")
    input("Presiona Enter para continuar...")

    os.system("cls")
    if (monto_ingresado != 0):
        print("Procesando el cambio")
        for i in range(8, 0, -1):
            print(f"⏳ {i} segundos restantes...")
            sleep(1)
        print("\n\n Tu vuelto es de:", monto_ingresado)
        input("Presiona Enter para continuar...")
        return True


while True:
    os.system("cls")
    try:
        golosina_seleccionada = monto_ingresado = None

        golosina_seleccionada = int(input(
            """¿Qué golosina quieres comprar? \n
           Selecciona el número:
           1 [Chocolate]: 5$
           2 [Caramelos]: 2$
           3 [Chicles]: 3$
           4 [Chupetas]: 6$
           5 Salir del programa
           \n\n\n > """   
        ))

        if golosina_seleccionada == 5:
            print("Saliendo del programa...")
            break;
        
        if golosina_seleccionada < 1 or golosina_seleccionada > 5:
            print(
                f"Opcion {golosina_seleccionada} no valida por favor elige una opcion valida")
            input("Presiona Enter para continuar...")
            continue
         
        monto_ingresado = int(input("Ingresa tu monto:"))
        os.system("cls")
        print("\n Procesando Entrega De Chucheria... \n")

        for i in range(5, 0, -1):
            print(f"⏳ {i} segundos restantes...")
            sleep(1)

        verificacion_golosina(golosina_seleccionada, monto_ingresado)

    except Exception as e:
        print("Ha ocurrido un error por favor verifica \n \n \n")
        input("Presiona Enter para continuar...")