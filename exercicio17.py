# Exercício 17 - Busca binária em códigos de produtos


def main():
    codigos = [101, 105, 110, 115, 120, 125, 130, 135]
    codigo = int(input("Digite o código do produto: "))

    inicio = 0
    fim = len(codigos) - 1
    encontrado = False

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if codigos[meio] == codigo:
            encontrado = True
            break
        elif codigo < codigos[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    if encontrado:
        print("Código cadastrado.")
    else:
        print("Código não cadastrado.")

if __name__ == "__main__":
    main()
