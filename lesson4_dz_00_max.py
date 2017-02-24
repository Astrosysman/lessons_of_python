#!/usr/bin/env python3

#Прогрвмма возврашает максимальный из введённых трёх чисел
#Автора Вазинский Виталий

from lesson4_dz_00_func_max import max_

def main():

	output = input('Введите число три числа через запятую: ')
	list_1 = (output.split(','))	
	list_ = [int(list_1[0]), int(list_1[1]), int(list_1[2])]	
	print(max_(list_))

main()
