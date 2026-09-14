# Exercício 21 - Buscar uma ocorrência em lista com valores repetidos


def main():
    numeros = [2, 4, 4, 4, 7, 9, 9, 12, 15]
    valor = int(input("Digite o valor procurado: "))

    inicio = 0
    fim = len(numeros) - 1
    posicao = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if numeros[meio] == valor:
            posicao = meio
            break
        elif valor < numeros[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    if posicao != -1:
        print("Uma ocorrência foi encontrada no índice:", posicao)
    else:
        print("Valor não encontrado.")

if __name__ == "__main__":
    main()
