# Exercício 4 - Buscar uma nota e contar ocorrências


def main():
    notas = [7.0, 8.5, 6.0, 7.0, 9.5, 7.0, 8.0]
    nota_procurada = float(input("Digite uma nota: "))

    quantidade = 0

    for nota in notas:
        if nota == nota_procurada:
            quantidade += 1

    if quantidade > 0:
        print("A nota aparece na lista.")
        print("Quantidade de ocorrências:", quantidade)
    else:
        print("A nota não aparece na lista.")

if __name__ == "__main__":
    main()
