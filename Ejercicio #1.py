def menu():
    print("Seleccione una opción:")
    print("1) Ejercicio 1: Juego de dados")
    print("2) Ejercicio 2: Grupos de alumnos")
    print("3) Ejercicio 3: Precio de entrada a la sala de juegos")
    print("4) Ejercicio 4: Contraseña")
    print("5) Salir")

def ejercicio_1():
    import random
    alvaro_puntaje = random.randint(1, 6)
    barbara_puntaje = random.randint(1, 6)
    print("Álvaro tira el dado y obtiene un puntaje de", alvaro_puntaje)
    print("Bárbara tira el dado y obtiene un puntaje de", barbara_puntaje)
    if alvaro_puntaje > barbara_puntaje:
        print("Álvaro gana")
    elif alvaro_puntaje < barbara_puntaje:
        print("Bárbara gana")
    else:
        print("Empate")

def ejercicio_2():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M/F): ").upper()
    if sexo == "M" and nombre < "N":
        print("Le corresponde el grupo A")
    elif sexo == "F" and nombre < "M":
        print("Le corresponde el grupo A")
    elif sexo == "M" and nombre > "N":
        print("Le corresponde el grupo B")
    elif sexo == "F" and nombre > "M":
        print("Le corresponde el grupo B")
    else:
        print("Opción incorrecta, vuelva a intentarlo.")

def ejercicio_3():
    edad = int(input("Ingrese la edad del cliente: "))
    if edad < 4:
        print("La entrada es gratis")
    elif 4 <= edad <= 18:
        print("Debe pagar la cantidad de 30000")
    else:
        print("Debe pagar la cantidad de 50000")

def ejercicio_4():
    contraseña = input("Ingrese la contraseña: ")
    while contraseña != "1234":
        print("Contraseña incorrecta, vuelva a intentarlo.")
        contraseña = input("Ingrese la contraseña: ")
    print("Contraseña correcta")

def ejercicio_5(cantidad_sin_iva, porcentaje_iva = 21):
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total

def generar_menu():
    opcion = None
    while opcion != '5':
        menu()
        opcion = input('Opción: ')
        if opcion == '1':
            ejercicio_1()
        elif opcion == '2':
            ejercicio_2()
        elif opcion == '3':
            ejercicio_3()
        elif opcion == '4':
            ejercicio_4()
        elif opcion == '5':
            print('Saliendo')
        else:
            print('Opción incorrecta, vuelva a intentarlo.')

if __name__ == "__main__":
    generar_menu()