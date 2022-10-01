# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Input a number greater than 0: '))
factorial = 1
if number < 0 or number == 0:
    print(f'The number "{number}" does not meet the conditions')
else:
    for i in range(1, number+1):
        factorial *= i
        print(factorial, end=' ')

