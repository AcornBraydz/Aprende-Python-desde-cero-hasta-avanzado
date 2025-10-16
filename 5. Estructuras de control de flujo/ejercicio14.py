numeros_pares = 0

i = 1
print ('\tInstrucciones: Suma los números pares del 1 al 10 y se detenga\n\tcuando la suma haya sobrepasado el límite de 15, por último \n\timprime el último resultado de la suma cuando se sobrepasó el límite.\n')
while i <= 10:
  if i % 2 == 0:
    print (f'-> {i}')
    numeros_pares += i
    if numeros_pares > 15:
      break
  i += 1
print (f'\nEl limite de 15 es: {numeros_pares}')