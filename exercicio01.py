# Exercício 1 - Busca sequencial em uma lista de 10 números


def main():
    numeros = [5, 12, 8, 23, 7, 19, 31, 4, 16, 10]
    valor = int(input("Digite um número para procurar: "))

    encontrado = False

    for numero in numeros:
        if numero == valor:
            encontrado = True
            break

    if encontrado:
        print("O número está presente na lista.")
    else:
        print("O número não está presente na lista.")

if __name__ == "__main__":
    main()
