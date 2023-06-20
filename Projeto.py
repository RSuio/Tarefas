n1 = float(input("Qual a sua nota nessa disciplina?"))
n2 = float(input("Qual a sua nota nessa disciplina?"))
n3 = float(input("Qual a sua nota nessa disciplina?"))
n4 = float(input("Qual a sua nota nessa disciplina?"))

soma = n1+n2+n3+n4

média = soma/4

if média >= 6:
    print("Parabens, voce está acima da média \nSua média é: {}".format(média))
else:
    print("Sua média está abaixo da requerida, não desanime e bons estudos!\nSua média é: {}".format(média))
