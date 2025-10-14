trabajadores = ["Ana García", "Carlos López", "María Rodríguez", "Pedro Martínez"]


solicitud_autorizador = True

if solicitud_autorizador == True:
  print ("---Trabajadores---")
  for trabajador in trabajadores:
    print (f'- {trabajador}')
else:
  print("No está autorizado para ver la información")
print ('-------------------\nFin del programa')