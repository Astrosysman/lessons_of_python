#!/usr/bin/env python3

#Функция print_list_even_1_not_even_0 заменяет чётные значения матрицы на "1", нечётные значения на "0"
#Автор Вазинский Виталий

def even(number):

	even = number % 2

	return  even == 0


def print_list_even_1_not_even_0(list_):


	for i in range(len(list_)):

		print('{}-'.format('--' * len(list_[i])))

		print(end='|')

		for j in range(len(list_[i])):

			if even(list_[i][j]):
				list_[i][j] = 1
			elif not even(list_[i][j]):
				list_[i][j] = 0

			print(list_[i][j],end='|')

		print()

	print('{}-'.format('--' * len(list_[i])))

