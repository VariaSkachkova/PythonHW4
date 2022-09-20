# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

nums = [1,1,1,1,2,2,2,3,3,3,4]
'''Создаем новый список и записываем в него только уникальные значения'''
def find_unique_values_in_list(nums):
    unique_nums = []
    for i in nums:
        if i not in unique_nums:
            unique_nums.append(i)
    return unique_nums

print(find_unique_values_in_list(nums))
