ancho = int(input("Ingrese el ancho del rectangulo:"))
altura = int(input("Ingresar la altura del rectangulo:"))
caracter = input("Ingresar el caracter a utilizar:")


def dibujar(an,al,letra):
    for i in range(an):
        for j in range(al):
            print(letra,end=" ")
        print()
        
dibujar(ancho,altura,caracter)
            
            
            