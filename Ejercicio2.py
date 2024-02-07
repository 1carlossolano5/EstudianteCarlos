def main():
    # Pedir al usuario que ingrese la cantidad de empleados
    num_empleados = int(input("Ingrese la cantidad de empleados: "))
    
    # Inicializar contadores y variable para almacenar el gasto total en sueldos
    empleados_entre_300k_y_10m = 0
    empleados_mas_de_3m = 0
    gasto_total = 0
    
    # Iterar sobre cada empleado para leer sus sueldos y actualizar los contadores y el gasto total
    for i in range(1, num_empleados + 1):
        sueldo = float(input(f"Ingrese el sueldo del empleado {i}: $"))
        gasto_total += sueldo
        if sueldo >= 300000 and sueldo <= 10000000:
            empleados_entre_300k_y_10m += 1
        if sueldo > 3000000:
            empleados_mas_de_3m += 1
    
    # Imprimir resultados
    print(f"\nCantidad de empleados que cobran entre $300.000 y $10.000.000: {empleados_entre_300k_y_10m}")
    print(f"Cantidad de empleados que cobran más de $3.000.000: {empleados_mas_de_3m}")
    print(f"Gasto total en sueldos: ${gasto_total:,.2f}")

if __name__ == "__main__":
    main()
