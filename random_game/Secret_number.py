numero = random.randint(1, 100)  # O 100 está incluso no sorteio

print("Qual é o seu nome?")
nome = input()
print("Olá", nome, "Vamos começar nosso jogo para adivinhar o número secreto!")

print("Qual seu primeiro palpite? escolha um número de 1 a 100")
palpite = int(input())
if palpite == numero:
    print("Uhuuu,", nome, "você conseguiu adivinhar o número secreto")
else:
    while palpite != numero:
        print("ops, não foi dessa vez")
        if palpite > numero:
            print("O número secreto é MENOR")
        else:
            print("O número secreto é MAIOR")
        print("Qual é o seu próximo palpite?")
        palpite = int(input())
    print("Parabééns,", nome, "!!!")
    print("você acertou o número secreto (" + str(numero) + ")")