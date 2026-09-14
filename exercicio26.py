# Exercício 26 - Controle de Estoque
# Comparação entre busca sequencial e busca binária


def main():
    codigos = [120, 105, 150, 110, 135, 125, 145, 100, 140, 130]
    codigo = int(input("Digite o código do produto: "))

    # Busca sequencial
    comparacoes_sequencial = 0
    posicao_sequencial = -1

    for i in range(len(codigos)):
        comparacoes_sequencial += 1
        if codigos[i] == codigo:
            posicao_sequencial = i
            break

    # Ordenação manual por seleção para usar busca binária
    ordenados = codigos.copy()

    for i in range(len(ordenados) - 1):
        menor = i
        for j in range(i + 1, len(ordenados)):
            if ordenados[j] < ordenados[menor]:
                menor = j

        temporario = ordenados[i]
        ordenados[i] = ordenados[menor]
        ordenados[menor] = temporario

    # Busca binária
    inicio = 0
    fim = len(ordenados) - 1
    comparacoes_binaria = 0
    posicao_binaria = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes_binaria += 1

        if ordenados[meio] == codigo:
            posicao_binaria = meio
            break
        elif codigo < ordenados[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    print("\nBusca sequencial:")
    print("Posição:", posicao_sequencial)
    print("Comparações:", comparacoes_sequencial)

    print("\nBusca binária:")
    print("Lista ordenada:", ordenados)
    print("Posição:", posicao_binaria)
    print("Comparações:", comparacoes_binaria)

if __name__ == "__main__":
    main()
