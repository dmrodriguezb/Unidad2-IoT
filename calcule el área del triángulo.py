#calcule el área del triángulo
def  calculaAreaTriangulo ( base , altura ):
    area = ( base * altura ) / 2
    print ( "El area del triangulo es:" , area )



base  =  float ( input ( "Ingrese la base del triangulo \ n " ))

altura  =  float ( input ( "Ingrese la altura del triangulo \ n " ))

calculaAreaTriangulo ( base , altura )
