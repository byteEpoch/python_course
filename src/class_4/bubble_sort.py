# Ordenamiento de burbuja. Más info aquí 👉🏻 https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja
import copy


def bubble_sort(nums):
    aux_nums = copy.copy(nums)
    while True:
        changed = False
        for i in range(len(aux_nums)):
            if i < (len(aux_nums) - 1) and (aux_nums[i] > aux_nums[i + 1]):
                aux_nums[i], aux_nums[i + 1] = aux_nums[i + 1], aux_nums[i]
                changed = True
        if not changed:
            break
    return aux_nums


print(bubble_sort([3, 5, 1, 8, 10, 2, 4]))
