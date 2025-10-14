a = 0b0011
a_binario = bin (a)
print (f'Valor original: {(a)}\nValor binario: {(a_binario)}')

# Aplica un desplazamiento de 2 posiciones a la izquierda.
a_left = a << 2

# Escribe el resultado en binario,Convierte ese resultado a decimal.
print (f'Valor resultado: {a_left}\nValor resultado en binario: {bin(a_left)}')