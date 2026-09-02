"""Crear un programa en Python que permita agregar, remover e imprimir información
de una pila de tipo string. La pila guardará los nombres de los departamentos  de  
Nicaragua  y  realizará  las  operaciones antes mencionadas con un menú de opciones y deberá usar métodos para cada caso.  """

class PilaDepartamentos:
    def __init__(self):
        self.pila = []
        self._precargar_departamentos()

    def _precargar_departamentos(self):
        """Carga inicial de las 17 entidades territoriales de Nicaragua."""
        entidades_iniciales = [
            "Boaco",
            "Carazo",
            "Chinandega",
            "Chontales",
            "Estelí",
            "Granada",
            "Jinotega",
            "León",
            "Madriz",
            "Managua",
            "Masaya",
            "Matagalpa",
            "Nueva Segovia",
            "RACCN (Región Autónoma del Caribe Norte)",
            "RACCS (Región Autónoma del Caribe Sur)",
            "Rivas",
            "Río San Juan"
        ]
        
        for entidad in entidades_iniciales:
            self.pila.append(entidad)

    def agregar(self, departamento: str):
        """Agrega un departamento al tope de la pila (Push)."""
        self.pila.append(departamento)
        print(f"✓ '{departamento}' ha sido agregado a la pila.")

    def remover(self):
        """Remueve y retorna el departamento del tope de la pila (Pop)."""
        if self.esta_vacia():
            print("⚠ La pila está vacía. No se puede remover ningún elemento.")
            return None
        departamento = self.pila.pop()
        print(f"✓ '{departamento}' ha sido removido de la pila.")
        return departamento

    def imprimir(self):
        """Muestra el contenido actual de la pila desde el tope hasta la base."""
        if self.esta_vacia():
            print("ℹ La pila se encuentra actualmente vacía.")
            return
        
        print("\n--- ESTADO DE LA PILA (Tope a Base) ---")
        for i, depto in enumerate(reversed(self.pila), 1):
            posicion = " [TOPE]" if i == 1 else ""
            print(f"{i:2d}. {depto}{posicion}")
        print("-" * 45)

    def esta_vacia(self) -> bool:
        """Verifica si la pila está vacía."""
        return len(self.pila) == 0


def mostrar_menu():
    """Muestra las opciones disponibles en consola."""
    print("\n====================================")
    print(" PILA DE DEPARTAMENTOS DE NICARAGUA ")
    print("====================================")
    print("1. Agregar departamento")
    print("2. Remover departamento")
    print("3. Imprimir pila")
    print("4. Salir")
    print("====================================")


def ejecutar_programa():
    pila_deptos = PilaDepartamentos()
    print("ℹ Se han precargado los 15 departamentos y 2 regiones autónomas de Nicaragua.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del departamento: ").strip().title()
            if nombre:
                pila_deptos.agregar(nombre)
            else:
                print("⚠ El nombre no puede estar vacío.")

        elif opcion == "2":
            pila_deptos.remover()

        elif opcion == "3":
            pila_deptos.imprimir()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("⚠ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()