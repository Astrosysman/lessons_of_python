#!/usr/bin/env python3

#Функция возвращает строку матрицы, сумма элементов которой максимальная
#Автор Вазинский Виталий

from lesson4_dz_00_func_max import max_

def print_list_max_sum_elements(list_):

	sum_list = [sum(list_[i]) for i in range(len(list_))]
	
	return list_[(sum_list.index(max_(sum_list)))]


	

