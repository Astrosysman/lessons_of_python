#!/usr/bin/env python3

#Функция переворачивает матрицу на 90 градусов налево
#Автор Вазинский Виталий

def print_rotate_90_left(list_):


	for i in range(len(list_) - 1, -1, -1):

		print('{}-'.format('----' * len(list_[i])))

		print(end='|')

		for j in range(len(list_[i])):

			print(list_[j][i],end='|')

		print()

	print('{}-'.format('----' * len(list_[i])))

