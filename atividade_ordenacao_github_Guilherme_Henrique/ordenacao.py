import random
import sys

sys.setrecursionlimit(5000)


def bubble_sort(vetor):
    comparacoes = 0
    trocas = 0
    n = len(vetor)

    for i in range(n - 1):
        houve_troca = False

        for j in range(n - 1 - i):
            comparacoes += 1

            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1
                houve_troca = True

        if not houve_troca:
            break

    return comparacoes, trocas


def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        if j + 1 != i:
            vetor[j + 1] = chave
            movimentacoes += 1

    return comparacoes, movimentacoes


def selection_sort(vetor):
    comparacoes = 0
    trocas = 0
    n = len(vetor)

    for i in range(n - 1):
        indice_menor = i

        for j in range(i + 1, n):
            comparacoes += 1

            if vetor[j] < vetor[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
            trocas += 1

    return comparacoes, trocas


def quick_sort(vetor):
    comparacoes = 0
    movimentacoes = 0

    def particionar(inicio, fim):
        nonlocal comparacoes, movimentacoes

        pivo = vetor[fim]
        i = inicio - 1

        for j in range(inicio, fim):
            comparacoes += 1

            if vetor[j] <= pivo:
                i += 1

                if i != j:
                    vetor[i], vetor[j] = vetor[j], vetor[i]
                    movimentacoes += 1

        if i + 1 != fim:
            vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
            movimentacoes += 1

        return i + 1

    def ordenar(inicio, fim):
        if inicio < fim:
            posicao_pivo = particionar(inicio, fim)
            ordenar(inicio, posicao_pivo - 1)
            ordenar(posicao_pivo + 1, fim)

    ordenar(0, len(vetor) - 1)

    return comparacoes, movimentacoes


random.seed(42)
tamanhos = [10, 20, 1000]
vetores_originais = {}

print("=" * 100)
print("EXPERIMENTO COM VETORES ALEATÓRIOS")
print("=" * 100)

for tamanho in tamanhos:
    original = random.sample(range(1, 100001), tamanho)
    vetores_originais[tamanho] = original.copy()

    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    bubble = bubble_sort(vetor_bubble)
    insertion = insertion_sort(vetor_insertion)
    selection = selection_sort(vetor_selection)
    quick = quick_sort(vetor_quick)

    print(f"\nTamanho: {tamanho}")
    print(f"Bubble Sort: {bubble[0]} comparações | {bubble[1]} trocas")
    print(f"Insertion Sort: {insertion[0]} comparações | {insertion[1]} movimentações")
    print(f"Selection Sort: {selection[0]} comparações | {selection[1]} trocas")
    print(f"Quick Sort: {quick[0]} comparações | {quick[1]} movimentações")


print("\n" + "=" * 100)
print("DESAFIO ADICIONAL")
print("=" * 100)

for tamanho in tamanhos:
    aleatorio = vetores_originais[tamanho].copy()
    ordenado = sorted(aleatorio)
    inverso = sorted(aleatorio, reverse=True)

    tipos = {
        "Aleatório": aleatorio,
        "Ordenado": ordenado,
        "Inverso": inverso
    }

    for nome, original in tipos.items():
        vetor_bubble = original.copy()
        vetor_insertion = original.copy()
        vetor_selection = original.copy()
        vetor_quick = original.copy()

        bubble = bubble_sort(vetor_bubble)
        insertion = insertion_sort(vetor_insertion)
        selection = selection_sort(vetor_selection)
        quick = quick_sort(vetor_quick)

        print(f"\nTamanho: {tamanho} | Organização: {nome}")
        print(f"Bubble: {bubble[0]} comparações | {bubble[1]} trocas")
        print(f"Insertion: {insertion[0]} comparações | {insertion[1]} movimentações")
        print(f"Selection: {selection[0]} comparações | {selection[1]} trocas")
        print(f"Quick: {quick[0]} comparações | {quick[1]} movimentações")
