# Función para encontrar el número máximo y mínimo de una lista.

def max_and_min(nums):
    max_num = nums[0]
    min_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num


print(max_and_min([3, 44, 100, 1, -7, 8999]))
