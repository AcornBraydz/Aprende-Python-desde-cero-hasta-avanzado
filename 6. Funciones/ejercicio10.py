# variable x global

x = 10


# Ahora como la global esta dentro de una funcion como global x
def var():
  global x
  x = 25
  print (x)

  
#  los cambios aplicados a x tambien se le hace a la x global de fuera por que se modifica en todo momento la global
var ()
print (x)