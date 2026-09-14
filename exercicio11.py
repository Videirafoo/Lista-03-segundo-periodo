# Exercício 11 - Buscar CPF e contar comparações


def main():
    cpfs = [
        "111.111.111-11",
        "222.222.222-22",
        "333.333.333-33",
        "444.444.444-44",
        "555.555.555-55"
    ]

    cpf = input("Digite o CPF: ")
    comparacoes = 0
    encontrado = False

    for item in cpfs:
        comparacoes += 1
        if item == cpf:
            encontrado = True
            break

    if encontrado:
        print("CPF cadastrado.")
    else:
        print("CPF não cadastrado.")

    print("Comparações realizadas:", comparacoes)

if __name__ == "__main__":
    main()
