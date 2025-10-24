numeros = list (range (1,11))

def externa (lista):
  def interna ():
    for indice , _ in enumerate (lista):
      print (f'{indice} - {_}')
  return interna

uvas = externa (numeros)
uvas()

