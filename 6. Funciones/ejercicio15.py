x = 10  # variable fuera de la función

def funcion_externa():
    global x
    print(f'Valor inicial de x = {x}')
    
    def funcion_interna():
        global x
        x += 1
        print(f'Dentro de la funcion interna x = {x}')
    
    funcion_interna()

# Llamadas múltiples
funcion_externa()  # x = 11
funcion_externa()  # x = 12
funcion_externa()  # x = 13
