numero  = int (input ('Ingresa un numero: '))

if numero > 0:
  print ('Es un numero positivo')
  if numero %2 == 0:
    print ('Es un numero par')
  else:
    print ('Es un numero impar')
elif numero < 0:
  print ('Es un numero negativo')
  if numero %3 == 0:
    print ('El numero es divisible entre 3')
else :
  print ('El numero es 0')
