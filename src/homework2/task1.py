"""
1. Напишите программу, которая считает общую цену.
   Вводится M рублей и N копеек цена, а также количество S товара.
   Посчитайте общую цену в рублях и копейках за L товаров.
"""


S = int(input('Количество товаров? '))
M = int(input('Введите количество рублей: '))
N = int(input('Введите количество копеек: '))

amount = ((M * 100 + N) * S)
print('Стоимость всех товаров:', amount // 100, 'рублей', amount % 100, 'копеек.')
