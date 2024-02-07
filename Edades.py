edades_mañana = 0
edades_tarde = 0
edades_noche = 0

for i in range(6):
    edad = int(input("Ingrese las edades de los estudiantes del turno de la mañana: "))
    edades_mañana += edad
    
for i in range(7):
    edad = int(input("Ingrese las edades de los estudiantes del turno de la tarde: "))
    edades_tarde += edad
    
for i in range(12):
    edad = int(input("Ingrese las edades de los estudiantes del turno de la noche: "))
    edades_noche += edad
    
promedio_mañana = edades_mañana / 6
promedio_tarde = edades_tarde / 7
promedio_noche = edades_noche / 12

print("Promedio estudiantes turno de la mañana", promedio_mañana)
print("Promedio estudiantes turno de la tarde", promedio_tarde)
print("Promedio estudiantes turno de la noche", promedio_noche)

if promedio_mañana > promedio_tarde and promedio_mañana > promedio_noche:
    print("Los estudiantes del turno de la mañana tienen un promedio de edades mayor")
elif promedio_tarde > promedio_mañana and promedio_tarde > promedio_noche:
    print("Los estudiantes del turno de la tarde tienen un promedio de edades mayor")
else:
    print("Los estudiantes del turno de la noche tienen un promedio de edades mayor")

