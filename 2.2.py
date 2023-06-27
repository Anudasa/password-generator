import random

length = int(input('Какой длины пароль: '))
password = ''
smbl = (",", "*", "'", "!", "^")
weight1 = [0, 1, 0, 0] #шансы какой будет символ для функции
weight2 = [0.1, 0, 0.8, 0.1] 
weight3 = [0, 0.38, 0.4, 0.02]
weight4 = [0.1, 0.22, 0.6, 0.08]

for i in range(length):
    number = str(random.randint(0, 9))
    letter_upper = chr(random.randint(65, 90))
    letter_lower = chr(random.randint(97, 122))
    symbol = random.choice(smbl)

    password_take = [number, letter_upper, letter_lower, symbol] # список символов для вложения в функцию
    password_symbol1 = random.choices(password_take, weights= weight1, k =1) # функция выбора символа
    password_symbol2 = random.choices(password_take, weights= weight2, k =1) # функция выбора символа 2 (Что бы первый элемент всегда был буквой)
    password += password_symbol1[0] # Добавление элемента в пароль
    password += password_symbol2[0]


print()
print('Ваш пароль: ', password)