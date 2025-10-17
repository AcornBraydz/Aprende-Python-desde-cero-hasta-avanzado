def contador ():
  cuenta = 0
  def incremento ():
    nonlocal cuenta
    cuenta += 1
    print (cuenta)
  return incremento

aumento = contador ()

for _ in range (4):
  aumento ()

