#!/usr/bin/env python3

# Возвращает первые десять простых чисел
# Автор Вазинский Виталий

def is_prime(number):

	inc = 2

	if number == 1:
		return False

	while number % inc !=0:
		inc += 1
	return number == inc

def main():

	num = count = 0
	while count < 10:
		num += 1
		if is_prime(num):
			count += 1
			print(num, end=' ')
	print()

main()
