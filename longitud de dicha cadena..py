#Programa que permita que dada una cadena tecleada por el usuario saber la longitud de dicha cadena. 
class cadena:
  def longitudCadena(self):
    x=input("Palabra: ")
    y=x.lower()
    y=y[0].upper()+y[1:]
    contador=0
    for i in x:
      contador+=1
    print(y,'tiene',contador,'caracteres.')

  

cadena=cadena()
cadena.longitudCadena()
