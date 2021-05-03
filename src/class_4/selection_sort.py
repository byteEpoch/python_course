# Ordenamiento por selección. Más info aquí 👉🏻 https://es.wikipedia.org/wiki/Ordenamiento_por_selecci%C3%B3n

def selection_sort(numbers):
    for i in range(len(numbers)):
        min_number_idx = i
        for j in range(i, len(numbers)):
            if numbers[min_number_idx] > numbers[j]:
                min_number_idx = j
        numbers[i], numbers[min_number_idx] = numbers[min_number_idx], numbers[i]
    return numbers


print(selection_sort([1, 5, 8, 2, 3, 0, 10, 4]))
