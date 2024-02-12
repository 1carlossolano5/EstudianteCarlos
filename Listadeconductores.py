Nombre_Conductores=[]
Kilometros_Diarios=[]
Total_kms=[]
Acum_kms=[]


Conductores=int(input("Ingrese la cantidad de conductores:"))

for x in range(Conductores):
    Nom=input("Por favor ingrese el nombre del conductor:")
    Nombre_Conductores.append(Nom)
    Acum_kms = 0
    
    for z in range(7):
        Kilometros=int(input("Ingrese la cantidad de kilometros diarios de cada conductor:"))
        Acum_kms = Acum_kms + Kilometros
        
    Total_kms.append(Acum_kms)
        
print("Los nombres de los conductores son:",Nombre_Conductores)
print("El total de kilometros recorridos es de:",Total_kms)

        
        
        

        
    

    
    
    
    

    



