print("********************************")
print("Bem-vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 43
numero_user = input("Digite o seu número: ")
numero_user_tratado = int(numero_user)

print("Você digitou ", numero_user)

if numero_secreto == numero_user_tratado:
    print("Você acertou!!")
else:
    print("Você errou =,)")
