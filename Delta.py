import math

def delta (a, b, c):
    return b ** 2 - 4 * a * c

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print ("A unica raiz é:{} ".format(raiz1))
    else:
        if d < 0:
            print(" Essa equação não possui raizes reais.")
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print("A primeira raiz é:{} ".format(raiz1))
            print("A segunda raiz é:{} ".format(raiz2))

def main():
    a = float(input("Digite um valor para a: "))
    b = float(input("Digite um valor para b: "))
    c = float(input("Digite um valor para c: "))
    imprime_raizes(a, b, c)

main()

