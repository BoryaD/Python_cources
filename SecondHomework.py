from __future__ import print_function
import base64
import numpy as np


def first_task(n):
    if not n.isdigit():
        print('Введено не число')
        return
    if n[-1] == '1':
        return 'Рубль'
    if n[-1] in ['2', '3', '4']:
        if len(n) == 2 and n[-2] == '1':
            return 'рублей'
        else:
            return 'рубля'
    if n[-1] in ['0', '5', '6', '7', '8', '9']:
        return 'рублей'


def second_task(n):
    if not n.isdigit():
        print('Введено не число')
        return
    if n[-1] == '1':
        return 'копейка'
    if n[-1] in ['2', '3', '4']:
        if len(n) == 2 and n[-2] == '1':
            return 'копеек'
        else:
            return 'копейки'
    if n[-1] in ['0', '5', '6', '7', '8', '9']:
        return 'копеек'


dict_hundreds = {'0': '', '1': 'сто', '2': 'двесте', '3': 'триста', '4': 'четыреста', '5': 'пятьсот', '6': 'шестьсот',
                 '7': 'семьсот', '8': 'восемьсот', '9': 'девятьсот'}
dict_external_dozens = {10: 'десять', 11: 'одиннадцать', 12: 'двеннадцать', 13: 'тринадцать', 14: 'четырнадцать',
                        15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',18: 'восемнадцать', 19: 'девятнадцать'}
dict_dozens = {'2': 'двадцать', '3': 'тридцать', '4': 'сорок', '5': 'пятьдесят', '6': 'шестьдесят', '7': 'семьдесят',
               '8': 'восемьдесят', '9': 'девяноста'}
dict_units = {'1': 'один', '2': 'двa', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
              '8': 'восемь', '9': 'девять'}


def third_task(n):

    if not n.isdigit():
        print('Введено не число')
        return
    if int(n) == 0:
        return 'Ноль'
    while True:
        if n[0] == '0':
            n = n[1::]
        else:
            break
    result = ''
    if len(n) > 3:
        raise ValueError('Мы ещё не умеем большие значения парсить')
    if len(n) == 3:
        result = dict_hundreds[n[0]]
        if 10 < int(n[1::]) < 19:
            result += ' ' + dict_external_dozens[int(n[1::])]
        else:
            result += ' ' + dict_dozens[n[1]]
            result += ' ' + dict_units[n[2]]
        return result
    if len(n) == 2:
        if 10 < int(n) < 19:
            result += ' ' + dict_external_dozens[int(n)]
        else:
            result += ' ' + dict_dozens[n[0]]
            result += ' ' + dict_units[n[1]]
        return result
    if len(n) == 1:
        return dict_units[n]


f_dict_units = {'1': 'одна', '2': 'две', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
              '8': 'восемь', '9': 'девять'}


def fourth_task(n):
    if not n.isdigit():
        print('Введено не число')
        return
    if int(n) == 0:
        return 'Ноль'
    while True:
        if n[0] == '0':
            n = n[1::]
        else:
            break
    result = ''
    if len(n) > 3:
        raise ValueError('Мы ещё не умеем большие значения парсить')
    if len(n) == 3:
        result = dict_hundreds[n[0]]
        if 10 < int(n[1::]) < 19:
            result += ' ' + dict_external_dozens[int(n[1::])]
        else:
            result += ' ' + dict_dozens[n[1]]
            result += ' ' + f_dict_units[n[2]]
        return result
    if len(n) == 2:
        if 10 < int(n) < 19:
            result += ' ' + dict_external_dozens[int(n)]
        else:
            result += ' ' + dict_dozens[n[0]]
            result += ' ' + f_dict_units[n[1]]
        return result
    if len(n) == 1:
        return f_dict_units[n]


def fifth_task(money):
    try:
        float(money)
    except:
        print("Введенные данные не корректны")

    money = money.split('.')
    res = third_task(money[0])
    res += ' ' + first_task(money[0])
    res += ' ' + fourth_task(money[1])
    res += ' ' + second_task(money[1])
    print(res)
    return res


def external_task(a, b):
    base64_symb = str(base64._b85alphabet)
    char_array = np.chararray((a, b))
    char_array[:] = '0'
    symb = 3
    prev_a = 0
    prev_b = 0
    while True:
        if a < 2 or b < 2:
            break
        if a < b:
            for i in range(prev_a, prev_a + a):
                for j in range(prev_b, prev_b + a):
                    char_array[i][j] = base64_symb[symb]
            b = b - a
            prev_b += a
        else:
            for i in range(prev_a, prev_a + b):
                for j in range(prev_b, prev_b + b):
                    char_array[i][j] = base64_symb[symb]
            a -= b
            prev_a += b
        symb += 1
        if symb == 65:
            symb = 3
    for i in char_array:
        print("\n")
        for j in i:
            print(str(j)[2], end="\t")







def main():
    n = input('Enter number for first task')
    print(first_task(n))
    n = input('Enter number for second task')
    print(second_task(n))
    n = input('Enter number for third task')
    print(third_task(n))
    n = input('Enter number for fourth task')
    print(fourth_task(n))
    n = input('Enter number for fifth task')
    fifth_task(n)
    external_task(64, 53)


if __name__ == "__main__":
    main()
