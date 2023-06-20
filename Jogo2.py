def computador_escolhe_jogada(n, m):
    jogada = 1
    while jogada <= m:
        if (n - jogada) % (m + 1) == 0:
            return jogada
        jogada += 1
    return m

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            print("Jogada inválida. Tente novamente.")
            jogada = 0
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vez_do_computador = False
    if n % (m + 1) == 0:
        vez_do_computador = False
        print("Você começa!")
    else:
        vez_do_computador = True
        print("Computador começa!")

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            print("O computador tirou", jogada, "peça(s).")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_do_computador = True
            print("Você tirou", jogada, "peça(s).")
        n -= jogada
        if n > 0:
            print("Agora restam", n, "peça(s) no tabuleiro.\n")

    if vez_do_computador:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0

def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):
        resultado = partida()
        if resultado == 1:
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\n**** Final do campeonato! ****")
    print("Placar: Computador", placar_computador, "X", placar_usuario, "Você")

print("Bem-vindo ao jogo do NIM!")
opcao = int(input("Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))

if opcao == 1:
    print("**** Partida Isolada ****")
    partida()
elif opcao == 2:
    print("Você escolheu um campeonato!")
    campeonato()
else:
    print("Opção inválida. O programa será encerrado.")
