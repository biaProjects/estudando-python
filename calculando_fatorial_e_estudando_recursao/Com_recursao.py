def fatorial(numero):
    print(f'Calculando fatorial de {numero}')
    if numero <= 1:
        print("Fatorial de", numero, "é 1 (caso base)")
        return numero
    else:
        resultado = numero * fatorial(numero-1)
        print("Fatorial de", numero, "é", resultado)
        return resultado


valor = int(input("Digite o número que você quer calcular o fatorial (n!) "))
fatorial(valor)