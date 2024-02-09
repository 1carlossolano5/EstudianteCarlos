añoinicial = int(input("Ingrese el año inicial"))
añofinal = int(input("Ingrese el año final"))

def año_bisiesto(año):
    if (año %4 == 0 and año % 100 !=0) or (año %400 ==0):
        print("El s")