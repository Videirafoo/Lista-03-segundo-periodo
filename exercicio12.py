# Exercício 12 - Busca sequencial com parada ao encontrar


def main():
    numeros = [3, 7, 12, 18, 25, 31, 44]
    valor = int(input("Digite o valor procurado: "))

    comparacoes = 0
    posicao = -1

    for i in range(len(numeros)):
        comparacoes += 1
        if numeros[i] == valor:
            posicao = i
            break

    if posicao != -1:
        print("Valor encontrado:", valor)
        print("Posição:", posicao)
    else:
        print("Valor não encontrado.")

    print("Comparações:", comparacoes)

if __name__ == "__main__":
    main()
