#!/usr/bin/env python3

first_number = float(input("Введите первое число:"))
second_number = float(input("Введите второе число:"))
third_number = float(input("Введите третье число:"))

numbers = [first_number, second_number, third_number]

if len(numbers) > len(list(set(numbers))):
	number_5 = [number + 5 for number in numbers]
	print("Введенные числа увеличены на 5: ", number_5, sep='\n')
else:
	print("Равных нет")
