#Usando secuencias de escape para tabular escribe una escalera de números del 1 al 10, el archivo se llamará iniciales_secuencia_escape.py. 
 
def  calculaAreaTriangulo ( base , altura ):
    area = ( base * altura ) / 2
    print ( "El area del triangulo es:" , area )



base  =  float ( input ( "Ingrese la base del triangulo \ n " ))

altura  =  float ( input ( "Ingrese la altura del triangulo \ n " ))

calculaAreaTriangulo ( base , altura )
