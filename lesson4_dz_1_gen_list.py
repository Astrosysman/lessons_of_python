#!/usr/bin/env python3

#Программа генерирует двухмерный рандомный массив в заданной размерностью
#Автор Вазинский Виталий

from lesson4_dz_1_func_gen_list import gen_list
import random

def main():

	number = int(input('Введите размерность списка: '))
	print(gen_list(number))

main()
