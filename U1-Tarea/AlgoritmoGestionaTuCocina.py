import os
import json
from datetime import datetime

# --- CLASES Y PROGRAMACIÓN ORIENTADA A OBJETOS (POO) ---

class Producto:
    """Clase base que representa un producto genérico en la cocina."""
    def __init__(self, nombre, cantidad, unidad, ubicacion, fecha_ingreso=None):
        # Encapsulamiento: atributos privados
        self.__nombre = nombre.strip().capitalize()
        self.__cantidad = float(cantidad)
        self.__unidad = unidad.strip().lower()
        self.__ubicacion = ubicacion.strip().lower()
        self.__fecha_ingreso = fecha_ingreso or datetime.now().strftime("%Y-%m-%d %H:%M")

    # Getters y Setters (Encapsulamiento)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad

    @property
    def unidad(self):
        return self.__unidad

    @property
    def ubicacion(self):
        return self.__ubicacion

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso

    def sumar_cantidad(self, extra):
        if extra > 0:
            self.__cantidad += extra

    def restar_cantidad(self, consumo):
        if 0 < consumo <= self.__cantidad:
            self.__cantidad -= consumo
            return True
        return False

    # Método base para polimorfismo
    def obtener_detalle(self):
        return f"{self.__ubicacion.upper()} - {self.__nombre}: {self.__cantidad} {self.__unidad}"

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "unidad": self.__unidad,
            "ubicacion": self.__ubicacion,
            "fecha_ingreso": self.__fecha_ingreso
        }


# Herencia: Subclase para productos de la alacena
class ProductoAlacena(Producto):
    def __init__(self, nombre, cantidad, unidad, fecha_ingreso=None):
        super().__init__(nombre, cantidad, unidad, "alacena", fecha_ingreso)

    # Polimorfismo: Sobrescribiendo el método de detalle
    def obtener_detalle(self):
        return f"[ALACENA] 📦 {self.nombre} -> {self.cantidad} {self.unidad}"


# Herencia: Subclase para productos del refrigerador
class ProductoRefrigerado(Producto):
    def __init__(self, nombre, cantidad, unidad, fecha_ingreso=None):
        super().__init__(nombre, cantidad, unidad, "refrigerador", fecha_ingreso)

    # Polimorfismo: Sobrescribiendo el método de detalle
    def obtener_detalle(self):
        return f"[REFRI] ❄️ {self.nombre} -> {self.cantidad} {self.unidad}"


class Inventario:
    """Clase encargada de administrar la colección de productos."""
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def agregar(self, producto):
        existente = self.buscar(producto.nombre)
        if existente:
            existente.sumar_cantidad(producto.cantidad)
            print(f"El producto ya existía. Nueva cantidad acumulada: {existente.cantidad} {existente.unidad}")
        else:
            self.productos.append(producto)
            print(f"¡Producto agregado con éxito: {producto.nombre}!")

    def buscar(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None

    def listar_ordenado(self):
        # Uso de operadores relacionales y funciones de ordenamiento por tuplas
        return sorted(self.productos, key=lambda p: (p.ubicacion, p.nombre))

    def guardar_inventario(self):
        try:
            datos = [p.to_dict() for p in self.productos]
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            print(f"Inventario guardado exitosamente en {self.archivo}.")
        except Exception as e:
            print(f"Hubo un error al guardar el archivo: {e}")

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.productos = []
                for d in datos:
                    tipo = d.get("tipo", "Producto")
                    # Reconstrucción de objetos según su clase específica
                    if tipo == "ProductoAlacena":
                        p = ProductoAlacena(d["nombre"], d["cantidad"], d["unidad"], d["fecha_ingreso"])
                    elif tipo == "ProductoRefrigerado":
                        p = ProductoRefrigerado(d["nombre"], d["cantidad"], d["unidad"], d["fecha_ingreso"])
                    else:
                        p = Producto(d["nombre"], d["cantidad"], d["unidad"], d["ubicacion"], d["fecha_ingreso"])
                    self.productos.append(p)
        except FileNotFoundError:
            print("No se encontró un archivo previo. Iniciando con inventario vacío.")
            self.productos = []
        except Exception:
            print("El archivo estaba dañado. Iniciando con inventario vacío.")
            self.productos = []


# --- FUNCIONES DE ENTRADA, SALIDA E INTERFAZ ---

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero <= 0:
                print("El número tiene que ser mayor que cero.")
                continue
            return numero
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("El campo no puede quedar vacío. Escribe algo.")
            continue
        return texto


def pedir_ubicacion():
    while True:
        lugar = input("¿Dónde está ubicado? (alacena/refrigerador): ").strip().lower()
        if lugar in ["alacena", "refrigerador"]:
            return lugar
        print("Opción no válida. Solo se permite 'alacena' o 'refrigerador'.")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA - GESTIONA TU COCINA")
    print("=" * 40)
    print("1. Ver inventario completo")
    print("2. Agregar nuevo producto")
    print("3. Consumir producto")
    print("4. Buscar producto específico")
    print("5. Ver productos por ubicación")
    print("6. Guardar y salir")
    print("=" * 40)

    while True:
        try:
            opcion = int(input("Elige una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            print("Esa opción no existe. Debe ser un número del 1 al 6.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


def main():
    inventario = Inventario()

    while True:
        limpiar_pantalla()
        opcion = mostrar_menu()

        if opcion == 1:
            if not inventario.productos:
                print("\nNo hay nada en el inventario todavía.")
            else:
                print("\n" + "=" * 50)
                print("                 INVENTARIO GENERAL")
                print("=" * 50)
                for p in inventario.listar_ordenado():
                    print(p.obtener_detalle())  # Polimorfismo aplicado aquí
                print("=" * 50)
            input("\nPresiona Enter para continuar...")

        elif opcion == 2:
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = pedir_texto("Nombre del producto: ")
            cantidad = pedir_numero("Cantidad: ")
            unidad = pedir_texto("Unidad de medida (kg, l, piezas, etc.): ")
            ubicacion = pedir_ubicacion()

            # Instanciación de objetos según la ubicación (Herencia)
            if ubicacion == "alacena":
                producto = ProductoAlacena(nombre, cantidad, unidad)
            else:
                producto = ProductoRefrigerado(nombre, cantidad, unidad)

            inventario.agregar(producto)
            input("\nPresiona Enter para continuar...")

        elif opcion == 3:
            print("\n--- CONSUMIR PRODUCTO ---")
            nombre = pedir_texto("Nombre del producto a consumir: ")
            producto = inventario.buscar(nombre)

            if not producto:
                print("No encontré ese producto en el inventario.")
            else:
                print(f"Producto: {producto.nombre}")
                print(f"Cantidad disponible: {producto.cantidad} {producto.unidad}")
                print(f"Ubicación: {producto.ubicacion}")

                cantidad_consumo = pedir_numero("¿Cuánto vas a consumir?: ")

                if cantidad_consumo > producto.cantidad:
                    print(f"No hay suficiente stock. Solo quedan {producto.cantidad} {producto.unidad}.")
                else:
                    producto.restar_cantidad(cantidad_consumo)
                    print(f"Operación exitosa. Queda un stock de: {producto.cantidad} {producto.unidad}")

                    if producto.cantidad == 0:
                        resp = input("El producto se agotó por completo. ¿Quieres borrarlo de la lista? (s/n): ").strip().lower()
                        if resp == 's':
                            inventario.productos.remove(producto)
                            print("El producto ha sido eliminado del inventario.")
            input("\nPresiona Enter para continuar...")

        elif opcion == 4:
            print("\n--- BUSCAR PRODUCTO ---")
            nombre = pedir_texto("Nombre del producto: ")
            producto = inventario.buscar(nombre)
            if producto:
                print("\n¡Lo encontré!")
                print(producto.obtener_detalle())
                print(f"Fecha de ingreso: {producto.fecha_ingreso}")
            else:
                print(f"No se encontró el producto '{nombre}'.")
            input("\nPresiona Enter para continuar...")

        elif opcion == 5:
            print("\n--- FILTRAR POR UBICACIÓN ---")
            ubicacion = pedir_ubicacion()
            encontrados = [p for p in inventario.productos if p.ubicacion == ubicacion]

            if not encontrados:
                print(f"No hay productos registrados en {ubicacion}.")
            else:
                print(f"\nProductos en {ubicacion.upper()}:")
                print("-" * 35)
                for p in encontrados:
                    print(f"- {p.nombre}: {p.cantidad} {p.unidad}")
                print("-" * 35)
                print(f"Total de registros: {len(encontrados)}")
            input("\nPresiona Enter para continuar...")

        elif opcion == 6:
            inventario.guardar_inventario()
            print("\n¡Nos vemos!")
            break


if __name__ == "__main__":
    main()