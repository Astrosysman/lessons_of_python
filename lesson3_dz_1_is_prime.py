#!/usr/bin/env python3

# Определяет является ли введёное число простым
# Автор Вазинский Виталий

def is_prime(number):

	inc = 2
	if number == 1:
		return False

	while number % inc !=0:
		inc += 1
	return number == inc

def main():
	number = int(input('Введите число: '))
	print(is_prime(number))

main()
