# Exercício 6 - Localizar o maior valor sem max() ou sort()


def main():
    numeros = [15, 8, 42, 3, 27, 19, 54, 11]

    maior = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero

    print("Lista:", numeros)
    print("Maior valor:", maior)

if __name__ == "__main__":
    main()
