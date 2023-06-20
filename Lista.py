def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista))  
    lista_sem_repeticao.sort()  
    return lista_sem_repeticao


lista = [2, 4, 2, 2, 3, 3, 1]
resultado = remove_repetidos(lista)
print(resultado) 
