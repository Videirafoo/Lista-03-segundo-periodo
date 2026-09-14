# Exercício 24 - Idade presente e quantidade de elementos descartados


def main():
    idades = [10, 12, 14, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50]
    idade = int(input("Digite a idade procurada: "))

    inicio = 0
    fim = len(idades) - 1
    posicao = -1
    descartados = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if idades[meio] == idade:
            posicao = meio
            break
        elif idade < idades[meio]:
            descartados += fim - meio + 1
            fim = meio - 1
        else:
            descartados += meio - inicio + 1
            inicio = meio + 1

    if posicao != -1:
        print("Idade encontrada no índice:", posicao)
    else:
        print("Idade não encontrada.")

    print("Elementos descartados durante a busca:", descartados)

if __name__ == "__main__":
    main()
