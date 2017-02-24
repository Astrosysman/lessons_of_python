#!/usr/bin/env python3

# Функция возвращает максимальный элемент из списка
# Автор Вазинский Виталий

def max_(list_):

	more  = list_[0]
	for i in list_:
        	if i > more:
                	more = i


	return more

