# AND dos 1 = 1
a = 0b1110
b = 0b1001
print(bin(a & b))

# OR un 1 al menos = 1
a = 0b0110
b = 0b1010
print(bin(a | b))


# XOR 2 diferentes = 1 ---- 2 iguales = 0
a = 0b1100
b = 0b1010
print(bin(a ^ b))

# Shift left
a = 0b0011
print(bin(a << 2))

# Shift right
a = 0b1100
print(bin(a >> 3))