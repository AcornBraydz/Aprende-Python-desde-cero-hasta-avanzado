#  Funciones anadidadas

def externa ():
  mensaje = 'Hola'
  def interna ():
    print (mensaje)
  interna ()
  def nome ():
    print (f'{mensaje} me gusta el coco')
  nome ()
externa ()