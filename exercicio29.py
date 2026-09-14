# Exercício 29 - Agenda Telefônica


def main():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel"]
    telefones = [
        "99999-1001",
        "99999-1002",
        "99999-1003",
        "99999-1004",
        "99999-1005",
        "99999-1006",
        "99999-1007"
    ]

    nome = input("Digite o nome do contato: ")

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
        print("Contato:", nomes[posicao])
        print("Telefone:", telefones[posicao])
    else:
        print("Contato não encontrado.")

if __name__ == "__main__":
    main()
