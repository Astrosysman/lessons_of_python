#!/usr/bin/env python3

#Функция переворачивает матрицу на 90 градусов направо
#Автор Вазинский Виталий

def print_rotate_90_right(list_):


	for i in range(len(list_)):

		print('{}-'.format('----' * len(list_[i])))

		print(end='|')

		for j in range(len(list_[i]) - 1, -1, -1):

			print(list_[j][i],end='|')

		print()

	print('{}-'.format('----' * len(list_[i])))

