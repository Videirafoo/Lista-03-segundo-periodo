# Exercício 15 - Busca binária em lista ordenada de nomes


def main():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel"]
    nome = input("Digite o nome procurado: ")

    inicio = 0
    fim = len(nomes) - 1
    posicao = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if nomes[meio].lower() == nome.lower():
            posicao = meio
            break
        elif nome.lower() < nomes[meio].lower():
            fim = meio - 1
        else:
            inicio = meio + 1

    if posicao != -1:
        print("Nome encontrado no índice:", posicao)
    else:
        print("Nome não encontrado.")

if __name__ == "__main__":
    main()
