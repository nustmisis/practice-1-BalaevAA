# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
try:
    weight = float(input())
    height = float(input())
except ValueError:
    print("Ошибка ввода данных")

BMI = weight / height**2
print(f'BMI = {BMI}')

if BMI < 18.5:
    t = "Дефицит"
elif 18.5 <= BMI < 24.9:
    t = "Норма"
elif 25 <= BMI < 29.9:
    t = "Предожирение"
else:
    t = "Ожирение"

print(f'Категория BMI: {t}')
