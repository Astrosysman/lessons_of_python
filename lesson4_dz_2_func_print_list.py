#!/usr/bin/env python3

#Функция выводит двухмерный массив в виде матрици
#Автор Вазинский Виталий

def print_list(list_):


	for i in range(len(list_)):

		print('{}-'.format('----' * len(list_[i])))

		print(end='|')

		for j in range(len(list_[i])):

			print(list_[i][j],end='|')

		print()

	print('{}-'.format('----' * len(list_[i])))

