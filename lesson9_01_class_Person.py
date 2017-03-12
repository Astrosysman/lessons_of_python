#!/usr/bin/env python3

from random import randint
from random import choice
from lesson9_01_list_name import *
		
def gen_person(list_name, list_surname):
	for _ in range(100):
		person_ = {

			'name': choice(list_name),
			'surname': choice(list_surname),
			'age': randint(0, 100),

		}
		
		yield person_

class Person:
	def __init__(self, name, surname, age):
		self.name = name
		self.surname = surname
		self.age = age

	def __str__(self):
		return 'Name: ' + self.name + '\nSurname: ' + self.surname + '\nAge: ' + str(self.age) + '\n'


def run():

	persons_list = []
	persons_list_name = []
	persons_list_surname = []
	persons_list_age = []
	
	person = gen_person(list_name, list_surname)

	try:

		while True:
			
			persons_list.append(next(person))
			
	except StopIteration:

		print('User list generated')
		print()

	for item in persons_list:
		person = Person(item['name'], item['surname'], item['age'])

		persons_list_name.append(item['name'])
		persons_list_surname.append(item['surname'])
		persons_list_age.append(item['age'])
		print(person)


	max_ = max(persons_list_age)
	min_ = min(persons_list_age)

	print('Oldest person - Name: {}, Surname: {}, Age: {}'.format(persons_list_name[persons_list_age.index(max_)], persons_list_surname[persons_list_age.index(max_)], persons_list_age[persons_list_age.index(max_)]))
	print()

	print('Youngest person - Name: {}, Surname: {}, Age: {}'.format(persons_list_name[persons_list_age.index(min_)], persons_list_surname[persons_list_age.index(min_)], persons_list_age[persons_list_age.index(min_)]))
	print()

if __name__ == "__main__":
	run()
