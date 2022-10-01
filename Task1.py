# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# Method1
# num = input("Input a number: ")
# sum = 0
# for digit in num:
#     if digit.isdigit():
#         sum += int(digit)
# print(f'Sum of digits = {sum}')

# Method2
number = abs(float(input('Input a number: ')))
sum_digits = 0
n = len(str(number)) - 2
number *= 10 ** n
while number > 0:
    sum_digits += number % 10
    number //= 10
print(f'Sum of digits = {int(sum_digits)}') #use 'int' to print number without fractional part 
