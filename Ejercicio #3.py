def calcular_el_precio(fruta, cantidad):
    precios_frutas = {
        "mango": 3000,
        "papaya": 2500,
        "piña": 3500,
        "aguacate": 4000,
        "limón": 2000
    }

    if fruta in precios_frutas:
        precio_unitario = precios_frutas[fruta]
        precio_total = precio_unitario * cantidad
        print(f"El precio total de {cantidad} {fruta}(s) es: ${precio_total}")
    else:
        print("Lo siento, esa fruta no se encuentra en nuestro inventario.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Consultar precio de una fruta")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fruta = input("Ingrese el nombre de la fruta: ").lower()
            cantidad = int(input("Ingrese la cantidad vendida: "))
            calcular_el_precio(fruta, cantidad)
        elif opcion == "2":
            print("Saliendo, hasta luego")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

def main():
    menu()


if __name__ == "__main__":
    main()
