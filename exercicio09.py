# Exercício 9 - Verificar matrícula de aluno


def main():
    matriculas = [202601, 202602, 202603, 202604, 202605]
    matricula = int(input("Digite a matrícula: "))

    cadastrado = False

    for numero in matriculas:
        if numero == matricula:
            cadastrado = True
            break

    if cadastrado:
        print("Aluno cadastrado.")
    else:
        print("Matrícula não encontrada.")

if __name__ == "__main__":
    main()
