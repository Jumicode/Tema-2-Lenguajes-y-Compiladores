# ------------------------------
# Descripción del Sistema
# ------------------------------

# La máquina está equipada con distintos ingredientes (leche, frutas, azúcar, hielo, etc.)
# en cantidades limitadas. Su funcionamiento se basa en las siguientes interacciones:
#
# - El usuario selecciona los ingredientes deseados desde un panel de cliente.
# - La máquina verifica si hay suficiente disponibilidad para cada ingrediente.
#   - Si falta algún ingrediente, se muestra un mensaje de advertencia y no se prepara la bebida.
#   - Si todos los ingredientes están disponibles, se procede con la mezcla durante 5 segundos.
#     Luego, se entrega el batido al usuario.
#
# - Existe un panel de operador que permite recargar los ingredientes cuando se agoten.
#
# Tipos de interacción humano-máquina:
# 1. Panel de Cliente: Permite al usuario seleccionar ingredientes y solicitar batidos.
# 2. Panel de Operador: Permite al operador reabastecer los ingredientes del sistema.



from os import system
from time import sleep


class Maquina:
    def __init__(self):

        self.leche_mililitros = 1000
        self.azucar_gramos = 1500
        self.fresa_gramos = 1500
        self.sandia_gramos = 1500
        self.melon_gramos = 1500
        self.guayaba_gramos = 1000
        self.hielo_gramos = 0

    def mostrar_la_cantidad_de_ingredientes_requeridos_por_marteada(self):
        print(""" \n Cantidad de ingredientes usados por bebida:""")
        print(f"""\n 1. Leche: 200ml""")
        print(f"""\n 2. Azucar: 50g""")
        print(f"""\n 3. Fresa: 100g""")
        print(f"""\n 4. Sandia: 100g""")
        print(f"""\n 5. Melon: 100g""")
        print(f"""\n 6. Guayaba: 100g""")
        print(f"""\n 7. Hielo: 50g\n\n""")

    def mostrar_ingredientes_disponibles(self):
        print(""" \n Ingredientes disponibles:""")
        print(f"""\n Leche: {self.leche_mililitros}ml""")
        print(f"""\n Azucar: {self.azucar_gramos}g""")
        print(f"""\n Fresa: {self.fresa_gramos}g""")
        print(f"""\n Sandia: {self.sandia_gramos}g""")
        print(f"""\n Melon: {self.melon_gramos}g""")
        print(f"""\n Guayaba: {self.guayaba_gramos}g""")
        print(f"""\n Hielo: {self.hielo_gramos}g \n\n""")

    def mostrar_Seleccion_de_ingredientes(self):
        print(""" \n Ingredientes:""")
        print("""\n 1. Leche""")
        print("""\n 2. Azucar""")
        print("""\n 3. Fresa""")
        print("""\n 4. Sandia""")
        print("""\n 5. Melon""")
        print("""\n 6. Guayaba""")
        print("""\n 7. Hielo""")
        print("""\n 8. volver al menu""")

    def rellenar_ingredientes(self, leche_mililitros, azucar_gramos, fresa_gramos, sandia_gramos, melon_gramos, guayaba_gramos, hielo_gramos):
        self.leche_mililitros += leche_mililitros
        self.azucar_gramos += azucar_gramos
        self.fresa_gramos += fresa_gramos
        self.sandia_gramos += sandia_gramos
        self.melon_gramos += melon_gramos
        self.guayaba_gramos += guayaba_gramos
        self.hielo_gramos += hielo_gramos

    def seleccion_ingredientes(self, seleccion):
        try:
            if 1 in seleccion and self.leche_mililitros < 200:
                print("\nNo hay suficiente Leche para preparar la bebida. \n")
                return True
            if 2 in seleccion and self.azucar_gramos < 50:
                print("\nNo hay suficiente Azúcar para preparar la bebida. \n")
                return True
            if 3 in seleccion and self.fresa_gramos < 100:
                print("\nNo hay suficiente Fresa para preparar la bebida. \n")
                return True
            if 4 in seleccion and self.sandia_gramos < 100:
                print("\nNo hay suficiente Sandía para preparar la bebida. \n")
                return True
            if 5 in seleccion and self.melon_gramos < 100:
                print("\nNo hay suficiente Melón para preparar la bebida. \n")
                return True
            if 6 in seleccion and self.guayaba_gramos < 100:
                print("\nNo hay suficiente Guayaba para preparar la bebida. \n")
                return True
            if 7 in seleccion and self.hielo_gramos < 50:
                print("\nNo hay suficiente Hielo para preparar la bebida. \n")
                return True

            for ingrediente in seleccion:
                if ingrediente == 1:
                    self.leche_mililitros -= 200

                elif ingrediente == 2:
                    self.azucar_gramos -= 50

                elif ingrediente == 3:
                    self.fresa_gramos -= 100

                elif ingrediente == 4:
                    self.sandia_gramos -= 100

                elif ingrediente == 5:
                    self.melon_gramos -= 100

                elif ingrediente == 6:
                    self.guayaba_gramos -= 100

                elif ingrediente == 7:
                    self.hielo_gramos -= 50

            return False

        except ValueError:
            print("Entrada inválida. Por favor, ingresa números válidos como se indica.")
            input("\n\nPresiona Enter para continuar...")
            return True

    def mezclar_ingredientes_y_servir(self):
        print(
            "Mezclando tus ingredientes seleccionados y sirviendo la bebida...")
        for i in range(5, 0, -1):
            print(f"⏳ {i} segundos restantes...")
            sleep(1)

        print("\n¡Tu bebida está lista para disfrutar!")
        input("\n\nPresiona Enter para continuar...")


maquina = Maquina()


class panel_cliente:
    def __init__(self):
        pass

    def seleccionar_ingredientes(self):
        system("cls")
        try:
            maquina.mostrar_la_cantidad_de_ingredientes_requeridos_por_marteada()

            input("\n\nPresiona Enter para continuar...")
            maquina.mostrar_ingredientes_disponibles()
            input("Presiona Enter para continuar...")

            print("\n\nSelecciona los ingredientes que deseas para tu bebida:")

            maquina.mostrar_Seleccion_de_ingredientes()

            seleccion = input(
                "\n\nIngresa los números de los ingredientes separados por comas (ejemplo: 1,2,3): ")

            seleccion = seleccion.split(',')
            seleccion = [int(seleccionado.strip())
                         for seleccionado in seleccion]

            if 8 in seleccion or 8 == seleccion:
                system("cls")
                return

            if (maquina.seleccion_ingredientes(seleccion)):
                print(
                    "No se puede preparar la bebida debido a la falta de ingredientes.")
                input("\n\nPresiona Enter para continuar...")
                system("cls")
                return

            maquina.mezclar_ingredientes_y_servir()
        except ValueError:
            system("cls")
            print("Entrada inválida. Por favor, ingresa números válidos como se indica.")
            input("\n\nPresiona Enter para continuar...")
            system("cls")


class panel_operador:
    def __init__(self):
        pass

    def rellenar_ingredientes(self):
        leche_mililitros = 0
        azucar_gramos = 0
        fresa_gramos = 0
        sandia_gramos = 0
        melon_gramos = 0
        guayaba_gramos = 0
        hielo_gramos = 0

        maquina.mostrar_ingredientes_disponibles()

        maquina.mostrar_Seleccion_de_ingredientes()

        try:
            SeleccionDeIngrediente = int(
                input("\n Selecciona el número del ingrediente a recargar:"))

            if SeleccionDeIngrediente == 8:
                system("cls")
                return

            if SeleccionDeIngrediente < 1 or SeleccionDeIngrediente > 7:
                print("Selección inválida. Por favor, selecciona un número entre 1 y 7.")
                return

            if SeleccionDeIngrediente == 1:
                print("\n\n Seleccionaste Leche \n")
                leche_mililitros = int(input("Leche (mililitros): "))

            elif SeleccionDeIngrediente == 2:
                print("\n\n Seleccionaste Azúcar \n")
                azucar_gramos = int(input("Azúcar (gramos): "))

            elif SeleccionDeIngrediente == 3:
                print("\n\n Seleccionaste Fresa \n")
                fresa_gramos = int(input("Fresa (gramos): "))

            elif SeleccionDeIngrediente == 4:
                print("\n\n Seleccionaste Sandía \n")
                sandia_gramos = int(input("Sandía (gramos): "))

            elif SeleccionDeIngrediente == 5:
                print("\n\n Seleccionaste Melón \n")
                melon_gramos = int(input("Melón (gramos): "))

            elif SeleccionDeIngrediente == 6:
                print("\n\n Seleccionaste Guayaba \n")
                guayaba_gramos = int(input("Guayaba (gramos): "))

            elif SeleccionDeIngrediente == 7:
                print("\n\n Seleccionaste Hielo \n")
                hielo_gramos = int(input("Hielo (gramos): "))

            else:
                print("Opción inválida")

            maquina.rellenar_ingredientes(leche_mililitros, azucar_gramos, fresa_gramos,
                                          sandia_gramos, melon_gramos, guayaba_gramos, hielo_gramos)

            print("\nIngredientes rellenados exitosamente.")
            input("\n\nPresiona Enter para continuar...")
            system("cls")
        except ValueError:
            system("cls")
            print("Entrada inválida. Por favor, ingresa datos válidos.")
            input("\n\nPresiona Enter para continuar...")
            system("cls")


while True:
    system("cls")
    print("\n Bienvenido al sistema de gestión de ingredientes para bebidas.")
    print("\n\n Selecciona una opción:")
    print("\n 1. Panel de Cliente")
    print("\n\n 2. Panel de Operador")
    print("\n\n 3. Salir del programa")

    opcion = int(input("\n\nIngresa el número de la opción: "))

    if opcion == 1:
        cliente = panel_cliente()
        cliente.seleccionar_ingredientes()

    if opcion == 2:
        operador = panel_operador()
        operador.rellenar_ingredientes()

    if opcion == 3:
        print("\n\n Vuelva Pronto \n\n...")
        exit()
