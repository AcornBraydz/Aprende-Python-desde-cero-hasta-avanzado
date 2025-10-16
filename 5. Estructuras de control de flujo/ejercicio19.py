

''' Permite ingresar dos números y realizar una división con
ellos, maneja las excepciones de valor, de división entre
cero, un error inesperado y por último indica que el programa se completó.'''

print ('\t\t------ Division entre dos numeros -----')

while True:

    # Ingresa el primer valor
  try:
    num_1 = int(input('Ingrese el numerador: '))
    break
  except ValueError:
    print ('valor invalido, solo numeros enteros')

while True:
    # Ingresa el segundo valor
  try:
    num_2 = int(input('Ingrese el denominador: '))
    print (f'Resultado de la division {num_1} / {num_2} = {num_1 / num_2:.2f}')
    print ('Termino del programa')
    break
  except ValueError:
    print ('valor invalido, solo numeros enteros')
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
  except Exception as error:
    print (F'Error inesperado {error}')



