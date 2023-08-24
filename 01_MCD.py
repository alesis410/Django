# 1. Escribir una función que calcule el máximo común divisor entre dos números

def mcd(a,b):
    mcd = 1

    if a % b == 0:
        return b
    
    for i in range(int(b/2),0,-1):
        if a % i == 0 and b % i == 0:
            mcd = i
            break

    return mcd

print(mcd(8,4))   
print(mcd(225,300))  