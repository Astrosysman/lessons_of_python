#!/usr/bin/env python3

#Программа возвращает минимальный из трёх введённых чисел
#Автор Вазинский Виталий

from lesson4_dz_00_func_min import min_

def main():

	output = input('Введите число три числа через запятую: ')
	list_1 = (output.split(','))	
	list_ = [int(list_1[0]), int(list_1[1]), int(list_1[2])]	
	print(min_(list_))

main()
