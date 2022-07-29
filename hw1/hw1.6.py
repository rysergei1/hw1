"""3 задача. Дана строка. Замените в этой строке все появления буквы h на букву H, 
кроме первого и последнего вхождения. 
Подсказка: использовать метод replace с параметрами. stroka.replace(a, b) — заменить в строке stroka все 
вхождения подстроки a на подстроку b.
если методу replace задать еще один параметр: stroka.replace(a, b, c), то заменены будут не все вхождения,
а только не больше, чем первые c штук из них"""

s = "hih hello"
first_occurrence = s[s.find("h")]
# print(s.find("h"))
# print(first_occurrence)
# last_occurrence = s[s.rfind("h")]
# print(last_occurrence)
slice_1 = s[s.find("h") + 1:s.rfind("h")]
slice_2 = s[s.rfind("h"):]
concatenation = first_occurrence + slice_1.replace("h", "H") + slice_2
print(f"До: hih hello\nПосле: {concatenation}")

# replace H
s = 'hih hello'
print(s.count('h'))
print((s.count('h')) - 1)
s = s.replace('h', 'H', s.count('h') - 1)
print(s)
s = s.replace('H', 'h', 1)
print(s)
