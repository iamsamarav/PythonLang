from random import randrange

print("********************************")
print("Bem-vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = int(randrange(0,101))
total_tentativas = 3
pontuacao = 1000

print("Qual nível de dificuldade")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_tentativas = 10
elif(nivel == 3):
    total_tentativas = 5
else:
    total_tentativas = 3

for rodada in range(1,total_tentativas + 1):
    numero_user = input("Digite o seu número entre e 100: ")
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    numero_user_tratado = int(numero_user)

    if(numero_user_tratado < 1 or numero_user_tratado > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue
    acertou = numero_user_tratado == numero_secreto
    maior_que = numero_user_tratado > numero_secreto
    menor_que = numero_user_tratado < numero_secreto

    print("Você digitou ", numero_user)

    if acertou:
        print("Você acertou!! E fez {} pontos".format(pontuacao))
        break
    else:
        if(maior_que):
            print("Você errou! O seu chute foi maior que o número secreto")
        elif(menor_que):
            print("Você errou! O seu chute foi menor que o número secreto")
        pontos_perdidos =  abs(numero_secreto - numero_user_tratado)
        pontuacao = pontuacao - pontos_perdidos


print("Fim do jogo")