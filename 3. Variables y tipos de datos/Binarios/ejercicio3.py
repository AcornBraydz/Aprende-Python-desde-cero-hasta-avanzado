# Pedir palabra al usuario

palabra = input ('Ingresa una palabra: ')

conversion = bytearray (palabra.encode('ascii'))

print (f'\n\tPalabra Original: {palabra}\n')

# Convertir 'X' a byte
print ('Remplazando el primer byte por X')
conversion[0] = ord ('X')
print (conversion)

print ('\nAgregar ! al final de la palabra')
# Agregar un signo de '!' al final
conversion.append(ord('!'))
print (conversion)
print (f"Palabra modificada: {conversion.decode('ascii')}")