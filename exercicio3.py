# Exercício 3 - Função de busca sequencial


def main():
    def busca_sequencial(lista, valor):
        for i in range(len(lista)):
            if lista[i] == valor:
                return i
        return -1


    numeros = [10, 20, 30, 40, 50]
    valor = int(input("Digite o valor que deseja buscar: "))

    indice = busca_sequencial(numeros, valor)

    if indice != -1:
        print("Valor encontrado no índice:", indice)
    else:
        print("Valor não encontrado.")

if __name__ == "__main__":
    main()
