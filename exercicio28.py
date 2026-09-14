# Exercício 28 - Comparação de desempenho


def main():
    numeros = list(range(1, 1001))
    valor = numeros[-1]

    # Busca sequencial
    comparacoes_sequencial = 0

    for numero in numeros:
        comparacoes_sequencial += 1
        if numero == valor:
            break

    # Busca binária
    inicio = 0
    fim = len(numeros) - 1
    comparacoes_binaria = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes_binaria += 1

        if numeros[meio] == valor:
            break
        elif valor < numeros[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Valor procurado:", valor)
    print("Comparações da busca sequencial:", comparacoes_sequencial)
    print("Comparações da busca binária:", comparacoes_binaria)

    print("\nConclusão:")
    print("A busca binária fez muito menos comparações porque elimina metade da lista a cada passo.")
    print("Porém, ela precisa que a lista esteja ordenada.")

if __name__ == "__main__":
    main()
