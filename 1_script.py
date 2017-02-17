#!/usr/bin/env python3

first_number = float(input("Введите первое число:"))
second_number = float(input("Введите второе число:"))

if first_number > second_number:
	print("Больше")
elif first_number < second_number:
	print("Меньше")
else:
	print("Эти числа равны")
