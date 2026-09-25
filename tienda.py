productos = {}
cantidad = int(input("¿Cuántos productos desea registrar? "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos[nombre] = precio

print("\n--- PRODUCTOS REGISTRADOS ---")

for nombre, precio in productos.items():
    print("Producto:", nombre, "- Precio: $", precio)

buscar = input("\nIngrese el nombre del producto que desea buscar: ")

if buscar in productos:
    print("El producto existe.")
    print("Precio: $", productos[buscar])
else:
    print("El producto no está registrado.")

eliminar = input("\nIngrese el nombre del producto que desea eliminar: ")

if eliminar in productos:
    del productos[eliminar]
    print("Producto eliminado correctamente.")
else:
    print("El producto no existe.")

print("\n--- LISTA ACTUALIZADA DE PRODUCTOS ---")

for nombre, precio in productos.items():
    print("Producto:", nombre, "- Precio: $", precio)