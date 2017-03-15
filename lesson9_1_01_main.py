#!/usr/bin/env python3

from random import randint
from random import choice
from lesson9_1_01_names import *
from lesson9_1_01_person import *

def gen_person(names, surnames):
	for _ in range(100):
		person = {

			'name': choice(names),
			'surname': choice(surnames),
			'age': randint(0, 100),

		}
		
		yield person

def main():
	
	persons = list(gen_person(names, surnames))

	for item in persons:
		person = Person(item['name'], item['surname'], item['age'])
		print(person)

	print('Oldest person - Name: {}, Surname: {}, Age: {}'.format(max(persons, key=lambda item: item['age'])['name'], max(persons, key=lambda item: item['age'])['surname'], max(persons, key=lambda item: item['age'])['age'],))
	print('Yougest person - Name: {}, Surname: {}, Age: {}'.format(min(persons, key=lambda item: item['age'])['name'], min(persons, key=lambda item: item['age'])['surname'], min(persons, key=lambda item: item['age'])['age'],))



if __name__ == "__main__":
	main()
