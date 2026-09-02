pila = []

def agregar_numero():
    numero = int(input("Ingrese un número entero: "))
    pila.append(numero)
    print("Número agregado.")

def contar_elementos():
    print("Cantidad de elementos en la pila:", len(pila))

def mostrar_elementos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elementos de la pila:")
        for numero in pila:
            print(numero)

def calcular_promedio():
    if len(pila) == 0:
        print("No hay elementos para calcular el promedio.")
    else:
        suma = sum(pila)
        promedio = suma / len(pila)
        print("El promedio es:", promedio)

def menu():
    opcion = 0
    while opcion != 5:
        print("\n***** Menú de Opciones *****")
        print("1. Agregar números")
        print("2. Contar elementos")
        print("3. Mostrar todos los elementos")
        print("4. Promedio de todos los números")
        print("5. Salir del sistema")

        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            agregar_numero()
        elif opcion == 2:
            contar_elementos()
        elif opcion == 3:
            mostrar_elementos()
        elif opcion == 4:
            calcular_promedio()
        elif opcion == 5:
            print("Saliendo del sistema...")
        else:
            print("Opción inválida, intente de nuevo.")

menu()