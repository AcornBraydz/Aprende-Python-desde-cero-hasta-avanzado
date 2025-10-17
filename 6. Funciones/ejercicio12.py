def un_funcion ():
  x = 10
  
  def segunda_funcion ():
    nonlocal x
    x = 20
    print (x)
  segunda_funcion ()

un_funcion ()