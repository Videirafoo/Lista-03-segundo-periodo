# Exercício 18 - Contar comparações da busca binária


def main():
    numeros = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    valor = int(input("Digite o valor procurado: "))

    inicio = 0
    fim = len(numeros) - 1
    comparacoes = 0
    posicao = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if numeros[meio] == valor:
            posicao = meio
            break
        elif valor < numeros[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    if posicao != -1:
        print("Valor encontrado no índice:", posicao)
    else:
        print("Valor não encontrado.")

    print("Comparações realizadas:", comparacoes)

if __name__ == "__main__":
    main()
