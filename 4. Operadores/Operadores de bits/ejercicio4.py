a = 0b1100 # 12
b = 0b1010 # 10
a_binario = bin (a)
b_binario = bin (b)
print (f'\tBinarios Originales:\na = {bin(a)}\nb = {bin(b)}\n')

# Escribe los valores de a y b en binario de 4 bits.
print (f'\tBinarios con 4 bits\na_4bits = {a_binario[2::]}\nb_4bits = {b_binario[2::]}\n')

# Aplica la operación XOR bit por bit: da 1 si los bits son diferentes, 0 si son iguales.

resultado_xor = a ^ b
print (f'Resultado en binario: {bin (resultado_xor)}\n')

print (f'Resultado en decimal: {resultado_xor}')
