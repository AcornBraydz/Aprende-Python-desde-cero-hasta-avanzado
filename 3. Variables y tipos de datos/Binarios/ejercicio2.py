# Pedir al usuario ingresar una palabra
palabra = input ('Ingresa una palabra: ')

# Conversion de palabra a bytes
byte = palabra.encode('ascii')

# imprimir cada byte y su caracter
for i in byte:
  print (f'Letra: {chr(i)} -> Byte: {i}')