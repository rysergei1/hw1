'''3.  Дано трехзначное число. Найдите сумму его цифр. Например, 123 - сумма 6, 545 - сумма 14,
 999 - сумма 27, 782 - сумма 17.'''

print("Введите трехзначное число и  нажмите ВВОД:")
number = int(input())
num = list(str(number))
# print(num)
a = num[0]
b = num[1]
c = num[2]
result = int(a) + int(b) + int(c)
print(f'Сумма цифр числа {number} = {result}')

#способ 2
d = number // 100
e = number // 10 % 10
f = number % 10
result_2 = d + e + f
print(result_2)
print("******")

# sum digits
num = 123
print(num % 10)
print(num // 10)
print((num // 10) % 10)
print(num // 100)
print(num % 10 + ((num // 10)) % 10 + num // 100)