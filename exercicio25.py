# Exercício 25 - Sistema de Biblioteca


def main():
    codigos_livros = [1001, 1005, 1010, 1012, 1020, 1025, 1030, 1040]
    codigo = int(input("Digite o código do livro: "))

    inicio = 0
    fim = len(codigos_livros) - 1
    posicao = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if codigos_livros[meio] == codigo:
            posicao = meio
            break
        elif codigo < codigos_livros[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    if posicao != -1:
        print("Livro disponível.")
        print("Posição na lista:", posicao)
    else:
        print("Código de livro não encontrado.")

if __name__ == "__main__":
    main()
