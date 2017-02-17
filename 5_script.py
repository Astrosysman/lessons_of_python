#!/usr/bin/env python3

you_name = input("Введите своё имя: ")
you_surname = input("Введите свою фамилию: ")
you_parto = input("Введите своё отчество: ")
you_group = input("Введите своё группу: ")

work1 = "Лабораторная работа №1"
work2 = "Выполнил(а) ст. гр " + you_group
work3 = you_name + " " + you_surname + " " + you_parto

len_work = [ len(work1), len(work2), len(work3) ]

print('{}'.format('*' * (max(len_work) + 4)))

for i in ( work1, work2, work3 ):
	print('{}{}{}{}'.format('* ', i,' ' * ( max(len_work) - len(i) + 1), '*' ))

print('{}'.format('*' * (max(len_work) + 4)))
