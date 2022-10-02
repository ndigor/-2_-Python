#1. Задача №1 -Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11
floatnumber = float(input(f'Введите вещественное(дробное) число'))
result=0
if floatnumber<0:
    floatnumber*=-1
    float_str=str(floatnumber)#Переводим число в строку
    for i in float_str:#суммируем в цикле все цифры числа
        if i!='.':
            result+=int (i)
            print (result)



