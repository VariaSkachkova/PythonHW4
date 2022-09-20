# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
num = 1534
''' Создаем список возможных простых множителей'''
def create_prime_factors_list (num):
    factors_list = []
    for i in range(2, num + 1):
        for j in factors_list:
            if i % j == 0:
                break
        else:
            factors_list.append(i)
    return factors_list
'''Находим все простые множители для данного числа'''
def find_prime_factors_of_int(num, factors_list):
    results_list = []
    while num != 1:
        for i in factors_list:
            if num % i == 0:                
                results_list.append(i)
                num = num / i
    return results_list
'''Убираем повторы из списка простых множителей'''
def leave_only_unique_factors(results_list):
    filtered_list = []
    for i in results_list:
        if i not in filtered_list:
            filtered_list.append(i)
    return filtered_list

filtered_list = leave_only_unique_factors(find_prime_factors_of_int(num, create_prime_factors_list (num)))
print(filtered_list)