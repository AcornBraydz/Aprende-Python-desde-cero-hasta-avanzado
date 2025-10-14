palabra = 'hola'
print (f'Palabra Original: {palabra}')
palabra = memoryview (bytearray (palabra.encode('ascii')))

for i in palabra:
  print (i)

print ('-----------')

#Agregamos un caracter a palabra
palabra [1] = ord ('X')

# Muestra los numeros en codigo ascii agregando la 'X'
for i in palabra:
  print (i)

# Pasamos de momoryview a bytearray para poder decodificar en ascii
palabra = bytearray(palabra)
palabra = palabra.decode('ascii')

# Mostrando la palabra modificada
print (f'Palabra modificada: {palabra}')