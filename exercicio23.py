# Exercício 23 - Última ocorrência usando busca binária


def main():
    numeros = [1, 2, 2, 2, 4, 5, 5, 7, 9]
    valor = int(input("Digite o valor procurado: "))

    inicio = 0
    fim = len(numeros) - 1
    ultima = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if numeros[meio] == valor:
            ultima = meio
            inicio = meio + 1
        elif valor < numeros[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    if ultima != -1:
        print("Última ocorrência no índice:", ultima)
    else:
        print("Valor não encontrado.")

if __name__ == "__main__":
    main()
