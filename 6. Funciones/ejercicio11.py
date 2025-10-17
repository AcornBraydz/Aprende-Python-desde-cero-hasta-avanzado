
contador = 0

def incrementar_contador ():
  global contador
  contador += 1
  print (contador)


# resetea a contador a 0
def resetear_contador ():
  global contador
  contador = 0
  print (contador)

def combo ():
  # Mandar a llamar incrementar_contador 5 veces
  for _ in range (5):
    incrementar_contador ()
  # Mandar a llamar resetear_contador
  resetear_contador ()

combo ()
