def maior_primo(numero):
    for n in range(numero, 1, -1):
        if eh_primo(n):
            return n

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(maior_primo(12)) 
print(maior_primo(28))  
print(maior_primo(49))  