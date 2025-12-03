numeros = list(range(1, 11))

def externa(lista):
    def interna():
        for indice, valor in enumerate(lista):
            # Ejemplos de ligaduras comunes en fuentes monoespaciadas
            print(f'{indice} -> {valor}')   # -> se convierte en una flecha
            print(f'{indice} => {valor}')   # => flecha doble
            print(f'{indice} != {valor}')   # != se convierte en ≠
            print(f'{indice} >= {valor}')   # >= se convierte en ≥
            print(f'{indice} <= {valor}')   # <= se convierte en ≤
    return interna

uvas = externa(numeros)
uvas()
