import importlib


def main():
    for numero in range(1, 31):
        modulo = importlib.import_module(f"exercicio{numero:02d}")

        print(f"\n===== EXECUTANDO O EXERCICIO {numero} =====")
        modulo.main()

    print("\nTodos os exercicios foram executados.")


if __name__ == "__main__":
    main()
