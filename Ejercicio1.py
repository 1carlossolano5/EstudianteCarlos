def calcular_promedio(alturas):
    # Calcular la suma de todas las alturas
    suma_alturas = sum(alturas)
    # Calcular la cantidad total de alturas
    cantidad_alturas = len(alturas)
    # Calcular el promedio
    promedio = suma_alturas / cantidad_alturas
    return promedio

def main():
    # Pedir al usuario que ingrese las alturas separadas por espacios
    alturas_input = input("Ingrese las alturas de las personas separadas por espacios: ")
    # Convertir la entrada en una lista de alturas (convertir strings a floats)
    alturas = [float(x) for x in alturas_input.split()]
    
    # Calcular el promedio de las alturas
    promedio_alturas = calcular_promedio(alturas)
    
    # Imprimir el promedio
    print(f"La altura promedio de las personas es: {promedio_alturas:.2f} unidades.")

if __name__ == "__main__":
    main()
