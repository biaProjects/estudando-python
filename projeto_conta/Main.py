from projeto_conta.Account import Conta

print("Iniciando sua conta bancária.")

titular = input("Digite seu nome: ")

conta = Conta(titular)

print("Olá,", conta.get_nome + ". Digite o valor que deseja depositar:")
Conta.deposito(conta, float(input()))
print("Seu saldo, após o depósito, é de: R$ %.2f" % conta.get_saldo)
print()

# 1 -> deposito | 2 -> saque | 0 -> sair
acao = 1
while acao != 0:
    print(f"Digite a operação que deseja realizar: \n1 para depósito \n2 para saque \n0 para sair de sua conta.")
    acao = int(input())

    if acao == 1:
        print("Ok! Agora, digite o valor que deseja depositar:")
        deposito = float(input())
        conta.deposito(deposito)
        print("Seu saldo, após o depósito, é de: R$ %.2f" % conta.get_saldo)
        print()

    elif acao == 2:
        print("Ok! Agora, digite o valor que deseja sacar:")
        saque = float(input())
        conta.saque(saque)
        print("Seu saldo, após o saque, é de: R$ %.2f" % conta.get_saldo)
        print()

    elif acao == 0:
        break

    else:
        print(f"Não é possivel realizar essa operação.")
        print(f"\nPor favor, digite 1 para deposito, 2 para saque ou 3 para sair da conta.\n")

print("Seu saldo final, após todas operações, é de R$ %.2f" % conta.get_saldo)
print("Obrigado por utilizar sua conta bancária!")