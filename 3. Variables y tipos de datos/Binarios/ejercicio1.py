# Tema: bytes,bytearay y memoryview

# Pedir una palabra al usuario
palabra = input ('Ingresa una palabra: ')

print ('Ejemplo con bytes')

# Convertir la palabra a bytes usando .encode
datos = palabra.encode('ascii')
# datos.add('P') no es posible por que ya esta convertido a byte y no se puede modificar
for i in datos:
  print (i)

palabrados = input ('Ingresa una nueva palabra: ')

print ('Ejemplo con bytearray')

datosdos = bytearray(palabrados.encode('ascii'))

for i in datosdos:
  print (i)
print ('Pero vamos a agregar un byte a mi palabra original')
datosdos.append(33) # ! -> se agrego el ! por que bytesarray si se puede modificar

print (datosdos)
aver = chr (datosdos[-1])
print (aver)
print ('Ejemplo con memoryview')

memoria = memoryview (datosdos)
print (memoria [1])