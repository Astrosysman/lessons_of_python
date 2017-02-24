#!/usr/bin/env python3

#Функция заменяет элементы главной диагонали матрицы на значение "0"
#Автор Вазинский Виталий

def print_list_diagonal_0(list_):


	for i in range(len(list_)):

		print('{}---'.format('----' * (len(list_[i]) - 1)))

		print(end='|')

		for j in range(len(list_[i])):

			if i == j:
				list_[i][j]=0

			print(list_[i][j],end='|')

		print()

	print('{}---'.format('----' * (len(list_[i]) - 1)))

