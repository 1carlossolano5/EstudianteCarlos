n = int(input("Ingrese # de empleados"))
cont= 0
cont1 = 0
Gasto = 0

for ini in range(n):
    Sueldo = float (input("Ingresar el valor sueldo del empleado: "))
    Gasto = Gasto+Sueldo
if Sueldo >=1300000 and Sueldo <=3000000:
    cont +=1
elif Sueldo > 3000000:
    cont1 +=1
print("Los gastos de las empresa total: ",Gasto)
print("Empleados que ganan entre 1.300.000 y 3.000.000 son: ",cont)
print("Empleados que ganan mas de 3.000.000 son: ",cont1)
    
    