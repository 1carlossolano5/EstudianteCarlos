texto="Buenos dias definiendo un parametro en una funcion"

def mensaje():
    N1= int(input("Ingresar el primer numero:"))
    N2= int(input("Ingresar el segundo numero:"))
    calcularmayor(N1,N2)
    positivo(N1,N2)
    
def calcularmayor(num1,num2):
    if num1>num2:
        print("El primer numero es el mayor")
    elif num1==num2:
        print("Son numeros iguales")
    else:
        print("El segundo numero es mayor")
        
def positivo(P1,P2):
    if P1>0 or P2>0:
        print("Numero positivo")
    elif P1<0 and P2<0:
        print("Son negativos")
    else:
        print("Al menos uno de los numeros no es positivo")
    
mensaje()