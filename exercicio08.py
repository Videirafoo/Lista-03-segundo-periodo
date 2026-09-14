# Exercício 8 - Retornar True ou False usando busca sequencial


def main():
    def existe_na_lista(lista, numero):
        for valor in lista:
            if valor == numero:
                return True
        return False


    numeros = [4, 9, 15, 21, 30]
    numero = int(input("Digite um número: "))

    print(existe_na_lista(numeros, numero))

if __name__ == "__main__":
    main()
