''' Instrucciones:
Escribe los valores de a y b en binario de 4 bits.

Aplica la operación AND bit por bit: solo da 1 si ambos bits son 1.

Escribe el resultado en binario.

Convierte ese resultado a decimal. '''


# valores
a = 0b1110
b = 0b1001

# Aplica la operación AND bit por bit: solo da 1 si ambos bits son 1.
AND = a & b
# Escribe los valores de a y b en binario de 4 bits.
a = bin (a)
b = bin (b)
# Escribe los valores de a y b en binario de 4 bits.
print (f'Binario 4 bits: \n{a [2::]}\n{b [2::]}')
print (f'Operacion AND: {bin(AND)}\nDecimal: {AND}')
