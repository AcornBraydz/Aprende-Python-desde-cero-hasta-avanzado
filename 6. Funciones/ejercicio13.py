x = 5
def funcion_exterior ():
  x = 10
  print (f'x dentro de funcion exterior {x}')
  def funcion_interior ():
    x = 3
    print (f'x dentro de funcion interior {x}')
  funcion_interior ()

print (f'x como global {x}')
funcion_exterior ()

# Ahora

def funcion_exterior ():
  x = 10 # variable local
  print (f'x dentro de funcion exterior {x}')
  def funcion_interior ():
    nonlocal x
    x = 6 # usa la variable local de funcion exterior 
    print (f'x dentro de funcion interior {x}')
  funcion_interior ()

print (f'x como global {x}')
funcion_exterior ()

# Ahora

def funcion_exterior ():
  x = 10 # variable local
  print (f'x dentro de funcion exterior {x}')
  def funcion_interior ():
    nonlocal x
    x = 6 # usa la variable local de funcion exterior 
    print (f'x dentro de funcion interior {x}')
  return funcion_interior

print (f'x como global {x}')
funcion_exterior ()
fn_interna = funcion_exterior ()
fn_interna ()
