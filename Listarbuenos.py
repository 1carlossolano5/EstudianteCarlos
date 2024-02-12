#Definir las listas
Nombres=[]
Notas=[]
AlumnoGod=[]
mb=0
b=0
iN=0

#Llenar la lista
for x in range(1,5):
    Nom = input(f"Por favor ingresar el nombre del alumno {x}: ")
    Nombres.append(Nom)
    No= int(input(f"Por favor ingresar las notas de los alumnos {x} : "))
    Notas.append(No)
#Recorrer la lista
for y in range(len(Nombres)):
    print(Nombres[y])
    print(Notas[y])
    
if Notas[y]>=8:
    print("Alumno muy bueno")
    mb += 1
    AlumnoGod.append(Nombres[y])
else:
    if Notas[y]>=4:
        print("Alumno bueno")
        b += 0
    else:
        print("Alumno no aprueba la materia")
        iN += 1
#Mostrar solo los alumnos que son alumnos buenos
eliminar=[]
for z in range(len(Notas)):
    if Notas[z]>=4 and Notas[z]<=7:
        ##Notas.pop(z)
        ##Nombres.pop(z)
        eliminar.append(z)
for d in sorted(eliminar,reverse=True):
    Notas
    
print("Cantidad de alumnos muy bueno son:",mb)
print("Nombre de los alumnos con la notas mas altas",AlumnoGod)
print("Listado de alumnos",Nombres[z])