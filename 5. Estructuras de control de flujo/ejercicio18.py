while True:
  try:
    entero = int(input ('Ingresa un numero para dividirlo entre 2: '))
    print ('resultado = ',entero/2)
    break

  except ValueError:
    print ('ingresa un numero valido')
  finally:
    print ('Que miras bobo')
    