#!/usr/bin/env python3

# Возвращает число Фибоначчи на ведёному пользователю номеру
# Автор Вазинский Виталий

def fibonacci_number(number):

	if number == 1 or number == 2:
		return 1

	return fibonacci_number(number - 2) + fibonacci_number(number - 1)

def main():
	number = int(input('Введите число: '))
	print(fibonacci_number(number))

main()
