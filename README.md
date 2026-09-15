# Lista 03 — Algoritmos de Busca em Python

Repositório acadêmico com **30 exercícios de Algoritmos e Estruturas de Dados**, focados em busca sequencial, busca binária e comparação entre estratégias.

**Nível:** intermediário  
**Objetivo:** entender como diferentes algoritmos de busca funcionam e por que a organização dos dados influencia o desempenho.

## O que você vai praticar

- busca sequencial;
- busca binária;
- contagem de comparações;
- listas ordenadas;
- primeira e última ocorrência;
- aplicações práticas de busca;
- comparação entre estratégias.

## Estrutura

```text
exercicio01.py
exercicio02.py
...
exercicio30.py
main.py
```

## Como executar

```bash
python exercicio01.py
```

Troque o número pelo exercício desejado.

## Como estudar

1. resolva primeiro com busca sequencial;
2. conte quantas comparações foram necessárias;
3. repita com busca binária quando os dados estiverem ordenados;
4. observe como `inicio`, `fim` e `meio` mudam;
5. explique quando vale a pena ordenar os dados antes de pesquisar.

## Conceito-chave

A busca binária é eficiente porque reduz o espaço de busca a cada etapa, mas depende de dados ordenados. A busca sequencial funciona mesmo sem ordenação, porém pode precisar percorrer muitos elementos.

## Desafio extra

Implemente um pequeno comparador que execute as duas buscas no mesmo conjunto de dados e mostre o número de comparações de cada algoritmo.

## Próximo passo

Depois desta lista, estude [lista-04-segundo-periodo](https://github.com/Videirafoo/lista-04-segundo-periodo), dedicada a recursividade.

## Qualidade

O GitHub Actions valida automaticamente a sintaxe dos arquivos Python.

## Tecnologias

`Python 3` · `Algoritmos` · `Estruturas de Dados` · `GitHub Actions`

## Autor

**Fernando Otávio Videira Junior**  
Engenharia de Software — Universidade de Vassouras, Campus Saquarema

> Não basta saber usar uma busca: o objetivo é entender o custo da estratégia escolhida.