persona = {
   "Nombre":"Carlos",
   "Apellido":"Solano",
   "Estatura":1.63,
   "Edad":20,
   "Email":"1carlossolano5@gmail.com", 
   "CiudadNac":"Bogotá",
   "Genero":["Femenino","Masculino","Otro"]
   
}
print(persona)
#Mostrar un elemento del diccionario
print("El nombre de la personas es:", {persona['Nombre']})
#Agregar elementos del diccionario
persona["Telefono"]=3134534534
print(persona)
#Modificar elemento del diccionario
persona["Telefono"]=2342342342
print(persona)
#Modificar la clave del elemento
persona["Celular"]=persona.pop("Telefono")
print(persona)
#Eliminar un elemento del diccionario
del persona["Celular"]
print(persona)

#Iterara los item de las claves y valores
for clave,valor in persona.items():
    print(clave, ":", valor)
