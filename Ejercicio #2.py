def añadir_numero_a_lista(lista):
    numero = int(input("Introduce un número para añadir a la lista: "))
    lista.append(numero)
    print("Número añadido a la lista.")

def añadir_numero_a_la_posicion(lista):
    numero = int(input("Introduce un número: "))
    posicion = int(input("Introduce la posición donde añadir el número (a partir de 1): ")) - 1
    lista.insert(posicion, numero)
    print("Número añadido en la posición", posicion + 1)

def longitud_de_lista(lista):
    print("Longitud de la lista:", len(lista))

def eliminar_ultimo_numero(lista):
    if lista:
        numero_eliminado = lista.pop()
        print("Número eliminado:", numero_eliminado)
    else:
        print("La lista está vacía.")

def eliminar_numero(lista):
    posicion = int(input("Introduce la posición del número a eliminar (a partir de 1): ")) - 1
    if 0 <= posicion < len(lista):
        numero_eliminado = lista.pop(posicion)
        print("Número eliminado:", numero_eliminado)
    else:
        print("Posición inválida.")

def contar_numeros(lista):
    numero = int(input("Introduce el número a contar: "))
    conteo = lista.count(numero)
    print("El número", numero, "aparece", conteo, "veces en la lista.")

def posiciones_numero(lista):
    numero = int(input("Introduce el número del cual quieres encontrar las posiciones: "))
    posiciones = [i + 1 for i, x in enumerate(lista) if x == numero]
    if posiciones:
        print("El número", numero, "se encuentra en las posiciones:", posiciones)
    else:
        print("El número", numero, "no está en la lista.")

def mostrar_numeros(lista):
    print("Números en la lista:", lista)

def main():
    lista = []
    while True:
        print("\nMenu:")
        print("1-Añadir número a la lista")
        print("2-Añadir número de la lista en una posición")
        print("3-Longitud de la lista")
        print("4-Eliminar el último número")
        print("5-Eliminar un número")
        print("6-Contar números")
        print("7-Posiciones de un número")
        print("8-Mostrar números")
        print("9-Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_numero_a_lista(lista)
        elif opcion == '2':
            añadir_numero_a_la_posicion(lista)
        elif opcion == '3':
            longitud_de_lista(lista)
        elif opcion == '4':
            eliminar_ultimo_numero(lista)
        elif opcion == '5':
            eliminar_numero(lista)
        elif opcion == '6':
            contar_numeros(lista)
        elif opcion == '7':
            posiciones_numero(lista)
        elif opcion == '8':
            mostrar_numeros(lista)
        elif opcion == '9':
            print("Saliendo :) .")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

