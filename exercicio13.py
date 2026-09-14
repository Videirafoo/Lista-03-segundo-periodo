# Exercício 13 - Busca binária manual


def main():
    numeros = [2, 5, 8, 12, 16, 20, 25, 31, 40, 50]
    valor = int(input("Digite o número procurado: "))

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
        print("Número encontrado no índice:", posicao)
    else:
        print("Número não encontrado.")

if __name__ == "__main__":
    main()
