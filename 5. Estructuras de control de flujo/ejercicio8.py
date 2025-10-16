
# ✈️ Vamos de viaje ✈️...!

##############################
#   Interfaz para usuario
##############################

print ('\t\tAreopuerto Good night\n- 1.Mexico\n- 2.Francia\n- 3.Roma\n- 4.Colombia\n----------------------')

destino = int (input ('Lugar para viajar: '))
edad = int (input('Edad: '))


##################################
#   Case con condiciones
##################################

match destino:
  case 1:
    mexico_precio = 16000
    print (f'Su vuelo a Mexico tiene un costo total de ${mexico_precio} mxn'if edad <= 30 else f'Su vuelo a Mexico tiene un costo total de ${mexico_precio-(mexico_precio*20/100)} mxn')
  case 2:
    francia_precio = 50000
    print (f'Su vuelo a Mexico tiene un costo total de ${francia_precio} mxn'if edad <= 30 else f'Su vuelo a Mexico tiene un costo total de ${francia_precio-(francia_precio*20/100)} mxn')
  case 3:
    roma_precio = 35000
    print (f'Su vuelo a Mexico tiene un costo total de ${roma_precio} mxn'if edad <= 30 else f'Su vuelo a Mexico tiene un costo total de ${roma_precio-(roma_precio*20/100)} mxn')
  case 4:
    colombia_precio = 12000
    print (f'Su vuelo a Mexico tiene un costo total de ${colombia_precio} mxn'if edad <= 30 else f'Su vuelo a Mexico tiene un costo total de ${colombia_precio-(colombia_precio*20/100)} mxn')
  case _:
    print ('Opcion invalida..!,Ingresa un numero valido')