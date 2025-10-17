def outer_func ():
  mensaje = 'Hola'
  def inner_func ():
    print (mensaje)
  inner_func ()


outer_func ()