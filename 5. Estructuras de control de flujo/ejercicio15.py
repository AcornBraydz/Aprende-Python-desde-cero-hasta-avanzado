# 5.6.1 Excepciones


print ('Division')

numero_uno = int (input('Ingresa el primer numero: '))
numero_dos = int (input('Ingresa el segundo numero: '))

division = numero_uno / numero_dos

if numero_dos == 0:
  raise ValueError('opcion invalida')
else:
  print (f'Resultado de la division: {division:.2f}')