#!/usr/bin/env python3

# Калькулятор
# Возвращает сумму, разницу, произведение, частное, квадратный корень, синус, косинус, возводит в степень двух введённых чисел
# Автор Вазинский Виталий

import math

def sqrt_(number1, number2):
	result1 = math.sqrt(number1)
	result2 = math.sqrt(number2)
	return result1, result2

def sin_(number1, number2):
	result1 = math.sin(math.radians(number1))
	result2 = math.sin(math.radians(number2))
	return result1, result2

def cos_(number1, number2):
	result1 = math.cos(math.radians(number1))
	result2 = math.cos(math.radians(number2))
	return result1, result2

def pow_(number1, number2):
	result = pow(number1,number2)
	return result

def add(number1, number2):
	result = number1 + number2
	return result

def sub(number1, number2):
	result = number1 - number2
	return result

def mull(number1, number2):
	result =  number1 * number2
	return result

def div(number1, number2):
	if number2 == 0:
		result = 'Div_zero'
		return result
	else:
		result = number1/number2
		return result

def main():
	your_choise = 'y'
	while your_choise == 'y' :
		number1 = float(input('Enter first number: '))
		number2 = float(input('Enter second number: '))
		operation = input('Enter your operation ( *, +, /, -, sin, cos, sqrt, pow ): ')

		if operation == '*':
			result = mull(number1, number2)
			print('{} * {} = {}'.format(number1, number2, result))
		elif operation == '/':
			result = div(number1, number2)
			if result == 'Div_zero':
				print('Division by zero')
			else:
				print('{} / {} = {}'.format(number1, number2, result))
		elif operation == '-':
			result = sub(number1, number2)
			print('{} - {} = {}'.format(number1, number2, result))
		elif operation == '+':
			result = add(number1, number2)
			print('{} + {} = {}'.format(number1, number2, result))
		elif operation == 'sqrt':
			result1, result2 = sqrt_(number1, number2)
			print('sqrt for {} = {}'.format(number1, result1))
			print('sqrt for {} = {}'.format(number2, result2))
		elif operation == 'pow':
			result = pow_(number1, number2)
			print('{} ** {} = {}'.format(number1, number2, result))
		elif operation == 'sin':
			result1, result2 = sin_(number1, number2)
			print('sin for {} = {}'.format(number1, result1))
			print('sin for {} = {}'.format(number2, result2))
		elif operation == 'cos':
			result1, result2 = cos_(number1, number2)
			print('cos for {} = {}'.format(number1, result1))
			print('cos for {} = {}'.format(number2, result2))
	
		your_choise = input('Repeat the operation("y" or "n"): ')

main()
