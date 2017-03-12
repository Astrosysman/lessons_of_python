#!/usr/bin/env python3


value = [4, 56, 23, 10]

def my_func_1(number):
	return number ** number

def my_func_2(number):
	return number + number

def gmap(func, value):
	for item in value:
		yield func(item)


def main():
	[ print (i) for i in gmap(my_func_1, value) ]
	[ print (i) for i in gmap(my_func_2, value) ]

if __name__ == "__main__":
	main()
