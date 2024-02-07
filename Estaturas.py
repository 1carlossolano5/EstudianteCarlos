def calcular_promedio(alturas):
    
    suma_alturas = sum(alturas)
    
    cantidad_alturas = len(alturas)
    
    promedio = suma_alturas / cantidad_alturas
    return promedio

def main():
    
    alturas_input = input("Ingrese las alturas de las personas separadas por espacios: ")
    
    alturas = [float(x) for x in alturas_input.split()]
    
    promedio_alturas = calcular_promedio(alturas)
    
    print(f"La altura promedio de las personas es: {promedio_alturas:.2f} unidades.")

if __name__ == "__main__":
    main()
