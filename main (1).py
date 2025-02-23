#UNIVERSIDAD ESTATAL AMAZÓNICA
#TAREA SEMANA 10
#PAMELA MORALES
import os
import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga el inventario desde un archivo."""
        if not os.path.exists(self.archivo):
            print("[INFO] Archivo de inventario no encontrado. Se creará uno nuevo.")
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.productos = json.load(f)
                print("[INFO] Inventario cargado correctamente.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"[ERROR] No se pudo cargar el inventario: {e}")
            self.productos = {}
        except PermissionError:
            print("[ERROR] No tienes permiso para acceder al archivo de inventario.")

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4)
            print("[INFO] Inventario guardado exitosamente.")
        except PermissionError:
            print("[ERROR] No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"[ERROR] No se pudo guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad):
        """Añade un producto al inventario."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_en_archivo()
        print(f"[INFO] Producto '{nombre}' añadido con éxito.")

    def actualizar_producto(self, nombre, cantidad):
        """Actualiza la cantidad de un producto."""
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_en_archivo()
            print(f"[INFO] Producto '{nombre}' actualizado con éxito.")
        else:
            print(f"[ERROR] Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_en_archivo()
            print(f"[INFO] Producto '{nombre}' eliminado con éxito.")
        else:
            print(f"[ERROR] Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("[INFO] El inventario está vacío.")
        else:
            print("Inventario actual:")
            for nombre, cantidad in self.productos.items():
                print(f"- {nombre}: {cantidad}")

# Ejemplo
inventario = Inventario()
inventario.agregar_producto("Manzanas", 10)
inventario.agregar_producto("Peras", 5)
inventario.actualizar_producto("Manzanas", 15)
inventario.eliminar_producto("Peras")
inventario.mostrar_inventario()
