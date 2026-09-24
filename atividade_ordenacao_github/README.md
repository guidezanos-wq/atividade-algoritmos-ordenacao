# Análise de Algoritmos de Ordenação

Atividade prática desenvolvida em Python para comparar a quantidade de operações realizadas pelos algoritmos:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort

Foram contabilizadas comparações e trocas/movimentações utilizando vetores de 10, 20 e 1000 elementos.

## Critério de contagem

- Comparação: cada comparação entre dois valores durante a ordenação.
- Bubble Sort: cada troca entre dois elementos conta como 1 troca.
- Selection Sort: cada troca entre duas posições conta como 1 troca.
- Insertion Sort: cada deslocamento conta como 1 movimentação e a reinserção da chave em outra posição também conta como movimentação.
- Quick Sort: cada troca entre duas posições durante o particionamento conta como 1 movimentação.

## Resultados

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 45 | 26 | 33 | 34 | 45 | 6 | 29 | 10 |
| 20 | 175 | 87 | 101 | 105 | 190 | 15 | 65 | 27 |
| 1000 | 498015 | 243076 | 244070 | 244070 | 499500 | 994 | 10234 | 4878 |

## Análise

### a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

O Quick Sort realizou o menor número de comparações, com 29 comparações.

### b) Qual algoritmo realizou menos trocas ou movimentações?

Para 10 elementos, o Selection Sort apresentou a menor quantidade, com 6 trocas.

### c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

Sim. O Quick Sort continuou apresentando menos comparações e o Selection Sort continuou apresentando poucas trocas.

### d) O que aconteceu quando o vetor passou para 1.000 elementos?

A quantidade de operações aumentou bastante nos algoritmos quadráticos. O Quick Sort permaneceu com um número de operações muito menor no vetor aleatório.

### e) Bubble Sort, Insertion Sort e Selection Sort apresentaram exatamente a mesma quantidade de operações?

Não. Apesar de terem complexidade O(n²) em situações típicas, cada algoritmo utiliza uma estratégia diferente e por isso a quantidade real de operações não é igual.

### f) Qual algoritmo apresentou maior crescimento no número de operações?

No experimento realizado, o Bubble Sort apresentou o maior crescimento considerando comparações e trocas.

### g) Como o comportamento do Quick Sort se diferenciou dos demais?

No vetor aleatório, o Quick Sort realizou muito menos operações, apresentando comportamento compatível com O(n log n) em média.

### h) Os resultados são coerentes com as complexidades teóricas?

Sim. Os algoritmos quadráticos cresceram muito mais rapidamente, enquanto o Quick Sort apresentou crescimento menor no vetor aleatório.

### i) Qual algoritmo seria escolhido para milhares de pedidos?

O Quick Sort, pois apresentou quantidade muito menor de operações no experimento com 1000 elementos aleatórios.

## Desafio adicional

Também foram testados:

- vetor aleatório;
- vetor já ordenado;
- vetor em ordem inversa.

A organização inicial interfere de maneiras diferentes nos algoritmos.

Bubble Sort e Insertion Sort se beneficiam muito quando o vetor já está ordenado. O Selection Sort mantém praticamente a mesma quantidade de comparações. Já o Quick Sort desta implementação usa o último elemento como pivô e pode atingir o pior caso O(n²) em vetores já ordenados ou em ordem inversa.

## Execução

```bash
python ordenacao.py
```

## Autora

Shayene Alves
