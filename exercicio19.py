# Exercício 19 - Busca binária retornando True ou False


def main():
    def busca_binaria(lista, valor):
        inicio = 0
        fim = len(lista) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if lista[meio] == valor:
                return True
            elif valor < lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1

        return False


    numeros = [5, 10, 15, 20, 25, 30, 35]
    valor = int(input("Digite um valor: "))

    print(busca_binaria(numeros, valor))

if __name__ == "__main__":
    main()
