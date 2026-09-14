# Exercício 16 - Exibir início, fim e meio em cada iteração


def main():
    numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
               22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

    valor = int(input("Digite o valor procurado: "))

    inicio = 0
    fim = len(numeros) - 1
    posicao = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        print("inicio =", inicio, "| fim =", fim, "| meio =", meio)

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

if __name__ == "__main__":
    main()
