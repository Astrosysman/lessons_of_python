#!/usr/bin/env python3

#Функция возвращает минимальный элемент списка
#Автор Вазинский Виталий

def min_(list_):

	less  = list_[0]
	for i in list_:
        	if i < less:
                	less = i


	return less

