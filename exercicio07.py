# Exercício 7 - Informar todas as posições de um valor


def main():
    import random

    numeros = []

    for i in range(15):
        numeros.append(random.randint(1, 10))

    print("Lista gerada:", numeros)

    valor = int(input("Digite um valor para procurar: "))
    posicoes = []

    for i in range(len(numeros)):
        if numeros[i] == valor:
            posicoes.append(i)

    if len(posicoes) > 0:
        print("O valor aparece nas posições:", posicoes)
    else:
        print("O valor não aparece na lista.")

if __name__ == "__main__":
    main()
