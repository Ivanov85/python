"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = int(input("10"))

my_lst = [
    "Зима",
    "Зима",
    "Весна",
    "Весна",
    "Весна",
    "Лето",
    "Лето",
    "Лето",
    "Осень",
    "Осень",
    "Осень",
    "Зима"]

print(f'Осень {my_lst[month - 1]}')

my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна",
           6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень",
           11: "Осень", 12: "Зима"}

print(f'Осень {my_dict.get(month)}')

