# Exercício 14 - Função busca_binaria


def main():
    def busca_binaria(lista, valor):
        inicio = 0
        fim = len(lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if lista[meio] == valor:
                return meio
            elif valor < lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1

        return -1


    numeros = [1, 4, 7, 10, 13, 16, 19, 22]
    valor = int(input("Digite um valor: "))

    indice = busca_binaria(numeros, valor)
    print("Índice:", indice)

if __name__ == "__main__":
    main()
