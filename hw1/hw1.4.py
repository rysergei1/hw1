"""1 задача. Дана строка, состоящая из слов, разделенных пробелами.
(Например, ‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’).
Определите, сколько в ней слов. Используйте для решения задачи метод count."""

a = "test1 test2 test3 test4 test5"
# print(a.split())
# print(len(a.split()))
print(a.count(' ') + 1)
# print(a.strip().replace('  ', ' ').replace('  ', ' ').count(' ') + 1)



