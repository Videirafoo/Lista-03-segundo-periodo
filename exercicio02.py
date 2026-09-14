# Exercício 2 - Buscar um nome e informar sua posição


def main():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"]
    nome_procurado = input("Digite um nome: ")

    posicao = -1

    for i in range(len(nomes)):
        if nomes[i].lower() == nome_procurado.lower():
            posicao = i
            break

    if posicao != -1:
        print("Nome encontrado na posição:", posicao)
    else:
        print("Nome não encontrado.")

if __name__ == "__main__":
    main()
