# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите номер дня недели:'))
if a > 7 :
    print('Нет такого дня недели')
elif 5 < a < 8 :
    print('Выходной')
else:
    print('Будний день')