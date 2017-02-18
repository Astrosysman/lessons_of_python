#!/usr/bin/env python3

# Возвращает количество разрядов введённого десятичного числа
# Автор Вазинский Виталий

def count_decimal_place(number):

	decimal_place = 0

	while number >= 1:
		number = number / 10
		decimal_place = decimal_place + 1
	return decimal_place

def main():
	
	number = int(input("Введите первое число: "))
	
	print(count_decimal_place(number))

main()
