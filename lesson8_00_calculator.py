#!/usr/bin/env python3

def add(a,d):
	return a + b

def sub(a,b):
	return a - b

def mul(a,b):
	return a * b

def div(a,b):
	return a / b

calculates = {

	'+':add,
	'-':sub,
	'*':mul,
	'/':div,

}

yet = ''
	
while yet != "n":

	try:
		a = int(input('a: '))
		b = int(input('b: '))
		operation = input()
		result = calculates[operation](a,b)

	except ValueError:
		print('Wrong value!!')
		continue

	except ZeroDivisionError:
		print('Division by zero!!')
		continue

	except Exception:
		print('Something wrong!!')
		continue

	else:
		print(result)

	finally:
		yet = input('Something else?("y" or "n", default "y"): ')
