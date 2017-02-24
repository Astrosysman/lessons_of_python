#!/usr/bin/env python3

#Программа выполняет следующие функции:
# 1. Генерирует матрицу 10х10
# 2. Выводит строку с максимальной суммой элементов
# 3. Переворачивает матрицу на 90 градусов налево
# 4. Переворачивает матрицу на 90 градусов направо
# 5. Заменяет элементы главной диагонали на "0"
# 6. Заменяет все чётные элементы на "1", а нечётные на "0"
# Автор Вазинский Виталий

import copy

from lesson4_dz_1_func_gen_list import gen_list
from lesson4_dz_2_func_print_list import print_list
from lesson4_dz_3_func_print_list_diagonal_0 import print_list_diagonal_0
from lesson4_dz_3_func_print_list_even_1_not_even_0 import print_list_even_1_not_even_0
from lesson4_dz_3_func_print_list_max_sum_elements import print_list_max_sum_elements
from lesson4_dz_3_func_print_rotate_90_left import print_rotate_90_left
from lesson4_dz_3_func_print_rotate_90_right import print_rotate_90_right

def main():

	list_gen_1 = gen_list(10)

	list_gen_2 = copy.deepcopy(list_gen_1)

	list_gen_3 = copy.deepcopy(list_gen_1)

	print('Исходная матрица:',end='\n')

	print_list(list_gen_1)

	print(end='\n\n')

	print('Строка элементов с максимальной суммой:',end='\n')

	print(print_list_max_sum_elements(list_gen_2))

	print(end='\n\n')

	print('Матрица, перевёрнутая на 90 градусов налево:',end='\n')

	print_rotate_90_left(list_gen_2)

	print(end='\n\n')

	print('Матрица, перевёрнутая на 90 градусов направо:',end='\n')

	print_rotate_90_right(list_gen_2)

	print(end='\n\n')

	print('Матрица с "0" по главной диагонали:',end='\n')

	print_list_diagonal_0(list_gen_2)

	print(end='\n\n')

	print('Матрица, в которой чётные числа заменены на "1", а нечётныe - "0":',end='\n')

	print_list_even_1_not_even_0(list_gen_3)

	print(end='\n\n')

main()
