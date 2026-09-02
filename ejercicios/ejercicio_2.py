 #Crear un programa en Python que permita guardar el primer nombre de las personas con las siguientes opciones de menú:
 
"""****Menú de Opciones*****
 
 1. Agregar un nombre a la Pila  
 2. Eliminar un nombre a la Pila  
 3. Mostrar el último elemento en la Cima  
 4. Buscar un elemento en la Pila  
 5. Contar cuantos elementos tiene la Pila  
 6. Mostrar todos los elementos de la pila  
 7. Limpiar la Pila  
 8. Salir  
 
 Nota: Los valores deben ser ingresados por teclado, además, debe usar funciones para todas las opciones de menú. """
 
 

import os

# Definimos la pila como una lista vacía

pila = []

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo (Windows o Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\n[ Presiona ENTER para regresar al menú ]")

def agregar():
    nombre = input("Escriba el nombre a agregar: ").strip()
    if nombre:
        pila.append(nombre)
        print(f"\n✓ SE AGREGÓ CORRECTAMENTE: '{nombre}'")
    else:
        print("\nx ERROR: No ingresaste ningún texto.")

def eliminar():
    if len(pila) == 0:
        print("\nx AVISO: La pila está vacía, no hay nada que eliminar.")
    else:
        borrado = pila.pop()
        print(f"\n✓ SE ELIMINÓ DE LA PILA: '{borrado}'")

def ver_cima():
    if len(pila) == 0:
        print("\nx AVISO: La pila está vacía.")
    else:
        print(f"\n→ ELEMENTO EN LA CIMA: {pila[-1]}")

def buscar():
    if len(pila) == 0:
        print("\nx AVISO: La pila está vacía.")
        return
    
    buscado = input("Nombre a buscar: ").strip()
    if buscado in pila:
        posicion = pila[::-1].index(buscado) + 1
        print(f"\n✓ ENCONTRADO: '{buscado}' está en la posición {posicion} (de la cima hacia abajo).")
    else:
        print(f"\nx NO ENCONTRADO: '{buscado}' no existe en la pila.")

def contar():
    print(f"\ni CANTIDAD TOTAL: La pila tiene {len(pila)} elemento(s).")

def ver_todos():
    if len(pila) == 0:
        print("\nx AVISO: La pila está vacía.")
    else:
        print("\n--- ELEMENTOS EN LA PILA (Desde la Cima hasta la Base) ---")
        for i, elem in enumerate(reversed(pila), 1):
            print(f"  {i}. [ {elem} ]")

def limpiar():
    if len(pila) == 0:
        print("\nx AVISO: La pila ya está vacía.")
    else:
        pila.clear()
        print("\n✓ LA PILA SE HA LIMPIADO POR COMPLETO.")

def main():
    while True:
        limpiar_pantalla()
        
        print("************************************")
        print("          MENÚ DE OPCIONES          ")
        print("************************************")
        print(f" ESTADO PILA ({len(pila)} elem): {pila}")
        print("------------------------------------")
        print("1. Agregar un nombre a la Pila")
        print("2. Eliminar un nombre a la Pila")
        print("3. Mostrar el último elemento en la Cima")
        print("4. Buscar un elemento en la Pila")
        print("5. Contar cuantos elementos tiene la Pila")
        print("6. Mostrar todos los elementos de la pila")
        print("7. Limpiar la Pila")
        print("8. Salir")
        print("************************************")
        
        opcion = input("\nSeleccione una opción (1-8): ").strip()
        print("\n" + "="*35)

        if opcion == "1":
            agregar()
            pausar()
        elif opcion == "2":
            eliminar()
            pausar()
        elif opcion == "3":
            mostrar_cima = ver_cima()
            pausar()
        elif opcion == "4":
            buscar()
            pausar()
        elif opcion == "5":
            contar()
            pausar()
        elif opcion == "6":
            ver_todos()
            pausar()
        elif opcion == "7":
            limpiar()
            pausar()
        elif opcion == "8":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("x Opción no válida. Digite un número entre 1 y 8.")
            pausar()

if __name__ == "__main__":
    main()