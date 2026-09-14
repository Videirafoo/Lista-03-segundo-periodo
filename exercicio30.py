# Exercício 30 - Menu completo de cadastro, ordenação e buscas


def main():
    valores = []
    lista_ordenada = False

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar valor")
        print("2 - Exibir lista")
        print("3 - Ordenar lista")
        print("4 - Busca sequencial")
        print("5 - Busca binária")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor: "))
            valores.append(valor)
            lista_ordenada = False
            print("Valor cadastrado.")

        elif opcao == "2":
            print("Lista:", valores)

        elif opcao == "3":
            # Ordenação manual por bolha
            for i in range(len(valores) - 1):
                for j in range(len(valores) - 1 - i):
                    if valores[j] > valores[j + 1]:
                        temporario = valores[j]
                        valores[j] = valores[j + 1]
                        valores[j + 1] = temporario

            lista_ordenada = True
            print("Lista ordenada:", valores)

        elif opcao == "4":
            valor = int(input("Digite o valor procurado: "))
            posicao = -1

            for i in range(len(valores)):
                if valores[i] == valor:
                    posicao = i
                    break

            if posicao != -1:
                print("Valor encontrado no índice:", posicao)
            else:
                print("Valor não encontrado.")

        elif opcao == "5":
            if not lista_ordenada:
                print("A busca binária só pode ser feita depois de ordenar a lista.")
            else:
                valor = int(input("Digite o valor procurado: "))
                inicio = 0
                fim = len(valores) - 1
                posicao = -1

                while inicio <= fim:
                    meio = (inicio + fim) // 2

                    if valores[meio] == valor:
                        posicao = meio
                        break
                    elif valor < valores[meio]:
                        fim = meio - 1
                    else:
                        inicio = meio + 1

                if posicao != -1:
                    print("Valor encontrado no índice:", posicao)
                else:
                    print("Valor não encontrado.")

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
