def externa ():
  numeros = []
  for i in range (1,6):
    numeros.append (i)
  suma = 0
  def interna ():
    nonlocal numeros
    nonlocal suma
    for _ in numeros:
      suma += _
      print (f'-> {suma}')
  return (interna)

bob = externa ()
bob ()