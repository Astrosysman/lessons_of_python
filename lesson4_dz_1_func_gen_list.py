#!/usr/bin/env python3

#Функция возвращает рандомный двухмерный массив, размерностью number X number
#Автор Вазинский Виталий

import random

def gen_list(number):

	random_list = [[random.randint(100, 999) for _ in range(number)] for _ in range(number)]

	return random_list

