def maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maximo(3, 5, 2))   
print(maximo(10, 2, 8))  
print(maximo(7, 7, 7))   
