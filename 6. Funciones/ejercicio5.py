''' Cuando usas un asterisco (*) en la definición de una función, estás diciendo que puede recibir una cantidad variable de argumentos.
Estos se agrupan automáticamente en una tupla. '''


def saludos (*superheroes):
  for i in superheroes:
    print (f'Un saludo para {i}')

saludos ('spiderman','batman','venom') 