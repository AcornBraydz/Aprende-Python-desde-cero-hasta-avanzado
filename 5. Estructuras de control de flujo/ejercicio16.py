# Prueba de try and except
##########################

try:
  a = 4/0
  numero = int(input ('Ingresa un numero: '))
except ZeroDivisionError:
  print ('No puedes dividir un numero entre 0')
