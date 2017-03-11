#!/usr/bin/env python3

class ExceptionEmployee(Exception):
	pass

class Employee:

	def __init__(self, name, surname, department, year_of_employment):
		departments = { 
			'IT',
			'Sales',
			'Transport',
			'Building',
		}
		
		year_of_foundation_of_the_company = 2005

		try:
			if year_of_foundation_of_the_company > year_of_employment:
				raise ExceptionEmployee
			elif department not in departments:
				raise ExceptionEmployee
			elif len(name) == 1 or len(name) > 30:
				raise ExceptionEmployee
			elif len(surname) == 1 or len(surname) > 30:

				raise ExceptionEmployee
		except ExceptionEmployee:
			return print('Please, enter correct info of employee')

		else:
			self.name = name
			self.surname = surname
			self.department = department
			self.year_of_employment = year_of_employment
			return print('Info of employee is correct')



def main():
	
	alex = Employee('Alex', 'Thomson', 'IT', 1999)
	john = Employee('John', 'Jackson', 'IT', 2009)
	o = Employee('O', 'Jackson', 'Building', 2005)
	e = Employee('Eve', 'Maliva', 'Finance', 2010)

if __name__ == "__main__":
	main()
