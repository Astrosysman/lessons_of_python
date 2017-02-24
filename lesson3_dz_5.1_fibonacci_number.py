#!/usr/bin/env python3

# Возвращает число Фибоначчи на ведёному пользователю номеру
# Автор Вазинский Виталий

def fibonacci_number(number):

	if number == 1 or number == 2:
		return 1

	return fibonacci_number(number - 2) + fibonacci_number(number - 1)

def fibonacci_number_1(number):
	first = second = 1
	buffer = None
	for _ in range(number):
		first, second = second, first + second

	return first

def main():
	number = int(input('Введите число: '))
	print(fibonacci_number(number))
	print(fibonacci_number_1(number))

main()
