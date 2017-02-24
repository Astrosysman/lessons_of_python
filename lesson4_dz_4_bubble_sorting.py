#!/usr/bin/env python3

#Программа выполняет сортировку списка пузырьковым методом
#Автор Вазинский Виталий

from lesson4_dz_4_func_bubble_sorting import bubble_sorting

def main():

	list_ = [5, 7, 23, 6, 78, 0, 1, 35]

	print('Не отсортированный список:')
	print(list_)
	print()

	print('Отсортированный список:')
	print(bubble_sorting(list_))

main()
