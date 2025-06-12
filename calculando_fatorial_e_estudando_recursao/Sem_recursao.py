numero = int(input("Digite o número que você quer calcular o fatorial (n!) "))

# controle
fatorial = 1
# valores que serão impressos
valores = [fatorial]
#valores dos fatoriais
fatoriais = []

# Caso de exceção:
if numero == 0:
    print(f'Calculando fatorial de {numero}')
    print(f'Fatorial de {numero} é 1 (caso base)')
# calculando
else:
    for numeros in range(2, numero+1):
        fatorial *= numeros
        fatoriais.append(fatorial)
        valores.append(numeros)

    valores = valores[::-1]

    for valor in valores:
        print(f'Calculando fatorial de {valor}')
    for i in range(1, numero + 1):
        if i == 1:
            print(f'Fatorial de {i} é 1 (caso base)')
        else:
            print(f'Fatorial de {i} é {fatoriais[-2+i]}')