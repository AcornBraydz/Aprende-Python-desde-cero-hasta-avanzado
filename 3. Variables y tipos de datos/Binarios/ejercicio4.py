palabra = input ('Ingresa una palabra: ')
# Conversion a bytes
palabra = palabra.encode ('ascii')
print (palabra)
# Conversion de bytes a caracter
palabra = palabra.decode ('ascii')
print (palabra)


lista = []
for i in palabra.encode('ascii'):
  i = bin (i)
  lista.append(i[2::])

print (f'Palabra Original: {palabra}')
print (f'Palabra en binario:\n{lista}')