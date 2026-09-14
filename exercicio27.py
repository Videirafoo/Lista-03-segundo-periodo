# Exercício 27 - Cadastro de Alunos


def main():
    matriculas = [202608, 202603, 202610, 202601, 202605, 202604, 202609]

    print("1 - Busca sequencial")
    print("2 - Busca binária")
    opcao = int(input("Escolha o tipo de busca: "))
    matricula = int(input("Digite a matrícula: "))

    if opcao == 1:
        posicao = -1

        for i in range(len(matriculas)):
            if matriculas[i] == matricula:
                posicao = i
                break

        if posicao != -1:
            print("Matrícula encontrada no índice:", posicao)
        else:
            print("Matrícula não encontrada.")

    elif opcao == 2:
        # Ordenação manual por bolha
        ordenadas = matriculas.copy()

        for i in range(len(ordenadas) - 1):
            for j in range(len(ordenadas) - 1 - i):
                if ordenadas[j] > ordenadas[j + 1]:
                    temporario = ordenadas[j]
                    ordenadas[j] = ordenadas[j + 1]
                    ordenadas[j + 1] = temporario

        inicio = 0
        fim = len(ordenadas) - 1
        posicao = -1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if ordenadas[meio] == matricula:
                posicao = meio
                break
            elif matricula < ordenadas[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1

        print("Lista ordenada:", ordenadas)

        if posicao != -1:
            print("Matrícula encontrada no índice:", posicao)
        else:
            print("Matrícula não encontrada.")

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
