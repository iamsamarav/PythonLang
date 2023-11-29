print("********************************")
print("Bem-vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 43
numero_user = input("Digite o seu número: ")
numero_user_tratado = int(numero_user)
acertou = numero_user_tratado == numero_secreto
maior_que = numero_user_tratado > numero_secreto
menor_que = numero_user_tratado < numero_secreto

print("Você digitou ", numero_user)

if acertou :
    print("Você acertou!!")
else:
    if(maior_que):
        print("Você errou! O seu chute foi maior que o número secreto")
    elif(menor_que):
        print("Você errou! O seu chute foi menor que o número secreto")
