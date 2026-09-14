# Exercício 10 - Encontrar a palavra com maior quantidade de caracteres


def main():
    palavras = ["casa", "computador", "python", "engenharia", "livro", "algoritmo"]

    maior_palavra = palavras[0]

    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    print("Palavras:", palavras)
    print("Palavra com mais caracteres:", maior_palavra)
    print("Quantidade de caracteres:", len(maior_palavra))

if __name__ == "__main__":
    main()
