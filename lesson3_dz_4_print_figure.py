#!/usr/bin/env python3

# Рисует фигуры "треугольник", "квадрат", "ромб", "лесница" с заданой пользователем размерностью
# Автор Вазинский Виталий

def print_triangle(number):

	limit = number

	for j in range(limit):
	    print('* ' * (limit - j))

	print("",end="\n\n")

	for j in range(limit + 1):
	    print('* ' * j)

	print("",end="\n\n")

	for j in range(limit):
	    for i in range(limit):
	        if limit -1 - j > i:
        	    print("  ", end='')
	        else:
        	    print("* ", end='')
	    print()

	print("",end="\n\n")

	for j in range(limit):
	    for i in range(limit):
        	if limit -1 - j < i:
	            print("  ", end='')
        	else:
	            print("* ", end='')
	    print()

	print("",end="\n\n")

	for j in range(limit):
	    for i in range(limit):
	        if j <= i:
        	    print("* ", end='')
	        else:
        	    print(" ", end='')
	    print()

	print("",end="\n\n")


	for j in range(limit):
	    for i in range(limit + 1):
	        if limit - j <= i:
	            print("* ", end='')
        	else:
	            print(" ", end='')
	    print()

def print_square(number):

	limit = number
	
	for i in range(limit):
		print('* ' * limit)

def print_romb(number):

	limit = number

	for j in range(limit):
	    for i in range(limit):
        	if limit - j <= i:
	            print("* ", end='')
        	else:
	            print(" ", end='')
	    print()

	for j in range(limit):
	    for i in range(limit):
        	if j <= i:
	            print("* ", end='')
        	else:
	            print(" ", end='')
	    print()

def print_ladder(number):

	print('{} {} {}'.format('Лесница на', number, 'ступенек'))

	limit = number * 2

	for j in range(limit + 1):

		bini = j%2
		step = j + bini

		print('{}{}'.format('  '* step, '* '))

		if bini == 0:

			print('{}{}'.format('  '* step, '* ' * 3))



def main():
	figure = input('Введите название фигуры("треугольник", "квадрат", "ромб", "лесница"): ').lower()
	number = int(input('Введите размерность фигуры: '))

	if figure == 'треугольник' or figure == 'triangle':
		print_triangle(number)

	elif figure == 'квадрат' or figure == 'square':
		print_square(number)

	elif figure == 'ромб' or figure == 'romb':
		print_romb(number)

	elif figure == 'лесница' or figure == 'ladder':
		print_ladder(number)

main()
