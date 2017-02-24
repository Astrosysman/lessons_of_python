#!/usr/bin/env python3

#Функция возвращает отсортированный по методу пузирьков список
#Автор Вазинский Виталий

def bubble_sorting(list_):

	length  = len(list_) - 1
	
	while length > 0:
		for i in range(length):
			if list_[i] > list_[i + 1]:
				buffer_ = list_[i]
				list_[i] = list_[i + 1]
				list_[i + 1] = buffer_

		length -= 1


	return list_

