while True:
  try:
    num_1 = int (input ('Ingresa 1er numero: '))
    num_2 = int (input ('Ingresa 2do numero: '))
    print (f'Resultado de {num_1} / {num_2} = {num_1/num_2}')
    break
  except ZeroDivisionError:
    print ('No es posible dividir un numero entre 0')
  except ValueError:
    print ('Solo puedes ingresar numeros, no letras o combinados') 