def vogal(caractere):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if caractere.lower() in vogais:
        return True
    else:
        return False

print(vogal('a'))  
print(vogal('b'))  
print(vogal('E'))  
print(vogal('x'))  
