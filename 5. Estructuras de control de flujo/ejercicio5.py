lenguaje = input ('Que lenguaje de programacion te gustaria aprender: ').lower().strip()

match lenguaje:
  case 'python':
    print ('Eres el futuro cientifico de datos')
  case _:
    print ('Opcion invalida')