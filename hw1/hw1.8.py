'''2.  Дано целое число. Найдите число десятков. Например, дано 12 - число десятков 1. Дано 58 - число десятков 5.
Дано 123 - число десятков 2. Дано 5839 - число десятков 3. Дано 7 - число десятков 0, дано 4 - число десятков 0. '''

number = [12, 58, 123, 5839, 7, 4]
for i in number:
    division_without_remainder = i // 10 # целочисленное деление без остатка на 10 - отбрасывается последняя цифра числа,
    # оставшееся последняя цифра и будет количество десятков, эту последнюю цифру нам нужно вывести через остаток от
    # деления.
    print(f'Промежуточный результат деления числа {i} без остатка на 10 равен числу: {division_without_remainder}')
    print(f'Дано число: {i} - число десятков {division_without_remainder % 10}')
    # Остаток от деления на 10 - это последняя цифра цисла (т.е. количества десятков после предыдущего
    # деления без остатка на 10). Если делимое меньше делителя, в частном получается ноль, а остаток равен делимому.

# 10-s count
n = 546
print(n // 10 % 10)