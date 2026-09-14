# Exercício 5 - Localizar produto e exibir preço


def main():
    produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]
    precos = [25.90, 8.50, 6.75, 5.80, 18.90]

    produto_procurado = input("Digite o nome do produto: ")

    indice = -1

    for i in range(len(produtos)):
        if produtos[i].lower() == produto_procurado.lower():
            indice = i
            break

    if indice != -1:
        print("Produto:", produtos[indice])
        print(f"Preço: R$ {precos[indice]:.2f}")
    else:
        print("Produto não encontrado.")

if __name__ == "__main__":
    main()
