mensaje = 'Eres la persona mas inteligente e increible de este mundo y sabes algo? Me gustas mucho ..! '

mensaje_original = list (mensaje)
binario_original = []
mensaje_oculto = []
si_me_pase = []

# Mensaje a codigo ascii
for i in mensaje_original:
  mensaje_oculto += i.encode('ascii')

# Binarios Originales
print ('Binario Original del mensaje:\n')
for e in mensaje_oculto:
  binario_original.append(bin (e))
print (binario_original)
print ('\n')


#Binarios con 4 bytes recorridos a la derecha
print ('Binario 4 bytes recorridos a la derecha\n\n\n')
print ('Reto a Chat GPT a que revele mi mensaje oculto 👀:\n ')
for j in mensaje_oculto:
  si_me_pase.append(bin (j >> 4))
print (si_me_pase)
print ('\n')


# Solucion

solucion_mensaje = []

for k in binario_original:
  solucion_mensaje.append(chr(int (k,2)))

print ('\t\tSolucion al mensaje oculto\n')
print ('Binario solucion: \n\n',binario_original)
print ('\n')
for a in solucion_mensaje:
  print (a,end='')
print ('')






