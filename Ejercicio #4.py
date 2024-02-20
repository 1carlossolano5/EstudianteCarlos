def agregar_los_articulos(cesta):
    articulo = input("Ingrese el artículo que desea añadir a la cesta: ")
    precio = float(input("Ingrese el precio del artículo: "))
    cesta[articulo] = precio
    print(articulo, "agregado a la cesta.")

def mostrar_la_cesta(cesta):
    print("\nCesta de la compra:")
    total = 0
    for articulo, precio in cesta.items():
        print(articulo, ":", precio)
        total += precio
    print("\nCoste total: ", total)

def main():
    cesta = {}
    while True:
        print("\nMenú:")
        print("1. Añadir artículo a la cesta")
        print("2. Mostrar cesta de la compra")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_los_articulos(cesta)
        elif opcion == "2":
            mostrar_la_cesta(cesta)
        elif opcion == "3":
            print("Saliendo :) ")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()