# 3) Задайте список из n чисел заполненный по формуле (1+1/n)^n
# и выведите на экран их сумму.

number = int(input('Input a number: '))
list = []
sum = 0
for i in range(1, number + 1):
    result = round((1 + 1 / i) ** i, 2)
    list.append(result)
    sum += result
print(list)
print(f'Sum of number = {round(sum, 2)}')
