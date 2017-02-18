#!/usr/bin/env python3

# Выводит на экран первые 'n' чётные числа
# Автор Вазинский Виталий

def even(number):

	even = number % 2

	return  even == 0

def main():
	number = int(input('Введите число: '))
	num = count = 0
	while count < number:
		num += 1
		if even(num):
			count += 1
			print(num, end=' ')
	print()

main()
