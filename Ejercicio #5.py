def ingreso_alumnos():
    num_alumnos = int(input("Ingrese el número de alumnos: "))
    alumnos = {}
    for _ in range(num_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print("Error: Este alumno ya ha sido ingresado.")
            continue
        num_notas = int(input(f"Ingrese la cantidad de notas para {nombre}: "))
        notas = []
        for i in range(num_notas):
            nota = float(input(f"Ingrese la nota {i + 1} para {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = notas
    return alumnos

def calcular_promedio(notas):
    if notas:
        return sum(notas) / len(notas)
    else:
        return 0

def mostrar_promedios(alumnos):
    print("\nPromedio de notas por alumno:")
    for alumno, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        print(f"{alumno}: {promedio:.2f}")

def main():
    alumnos = ingreso_alumnos()
    mostrar_promedios(alumnos)

if __name__ == "__main__":
    main()
