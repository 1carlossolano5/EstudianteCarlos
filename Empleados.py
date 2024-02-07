def main():
    num_empleados = int(input("Ingrese la cantidad de empleados: "))
    
    empleados_entre_1300000m_y_3000000m = 0
    empleados_mas_de_3000000m = 0
    gasto_total = 0
    
    for i in range(1, num_empleados + 1):
        sueldo = float(input(f"Ingrese el sueldo del empleado {i}: $"))
        gasto_total += sueldo
        if sueldo >= 1300000 and sueldo <= 3000000:
            empleados_entre_1300000m_y_3000000m += 1
        if sueldo > 3000000:
            empleados_mas_de_3000000m += 1
    
    print(f"Cantidad de empleados que cobran entre $1.300.000 y $3.000.000: {empleados_entre_1300000m_y_3000000m}")
    print(f"Cantidad de empleados que cobran más de $3.000.000: {empleados_mas_de_3000000m}")
    print(f"Gasto total en sueldos: ${gasto_total:,.2f}")

if __name__ == "__main__":
    main()
