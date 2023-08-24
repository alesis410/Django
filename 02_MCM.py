# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números


def mcm(a,b):
    # buscamos el numero mayor
    c = max(a,b)
# se crea bucle sumando +1 hasta que en ambos numeros el resto sea 0
    while True:
        if c % a == 0 and c % b == 0 :
            return c
        
        c += 1

print(mcm(4,3))
