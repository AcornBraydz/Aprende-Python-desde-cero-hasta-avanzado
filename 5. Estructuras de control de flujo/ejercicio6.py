edad = int (input ('Ingresa tu edad: '))


match edad:
  case edad if 0 < edad <= 11:
    edad = 'Niño'
    print ('Clasificacion de edad: Niño')
    print (f'Estas en la etapa de {edad}!')
  case edad if 12 <= edad <= 17 :
    edad = 'Adolescente'
    print ('Clasificacion de edad: Adolescente')
    print (f'Estas en la etapa de {edad}!')
  case edad if 18 <= edad <= 59:
    edad = 'Adulto'
    print ('Clasificacion de edad: Adulto')
    print (f'Estas en la etapa de {edad}!')
  case _:
    edad = 'Adulto mayor'
    print ('Clasificacion de edad: Adulto mayor')
    print (f'Estas en la etapa de {edad}!')

