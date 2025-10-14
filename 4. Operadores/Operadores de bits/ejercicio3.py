a = 0b0110
b = 0b1010

print (f'Valores Originales antes del OR:\na = {bin (a)}\nb = {bin (b)}')
# sacamos el resultado con OR
resultado_decimal = a | b
resultado = bin (resultado_decimal)
print (f'Resultado de OR:\nBinario: {resultado[2::]}\nDecimal: {resultado_decimal}')