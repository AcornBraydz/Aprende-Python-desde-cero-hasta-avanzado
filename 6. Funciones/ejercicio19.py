numeros = []

for i in range (1,51):
  numeros.append (i)


def funcion_externa ():
  global numeros
  def funcion_interna ():
    for indice,_ in enumerate(numeros):
      print (f'-> indice: {indice} - valor de la lista: {_}')
  return funcion_interna

bob  = funcion_externa ()
bob ()