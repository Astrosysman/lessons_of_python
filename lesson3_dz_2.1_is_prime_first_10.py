#!/usr/bin/env python3

# Возвращает первые десять простых чисел
# Автор Вазинский Виталий

from lesson3_dz_2_is_prime_first_10 import is_prime

def main():

	num = count = 0
	while count < 10:
		num += 1
		if is_prime(num):
			count += 1
			print(num, end=' ')
	print()

if __name__ == '__main__':
	main()
