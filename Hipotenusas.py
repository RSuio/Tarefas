def é_hipotenusa(num):
    for i in range(1, num):
        for j in range(i, num):
            if i**2 + j**2 == num**2:
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for num in range(1, n+1):
        if é_hipotenusa(num):
            soma += num
    return soma
