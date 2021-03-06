#!/usr/bin/env python3

from random import randint
from random import choice
from lesson9_2_01_names import *
from lesson9_2_01_person import *

def gen_person(names, surnames):
	for _ in range(100):
		person = {

			'name': choice(names),
			'surname': choice(surnames),
			'age': randint(0, 100),

		}
		
		yield person

def main():
	
	list_persons = [ Person(person['name'], person['surname'], person['age']) for person in gen_person(names, surnames) ]

	for item in list_persons:
		print(item)

	max_person_age = max(list_persons, key=lambda item: item.age)
	min_person_age = min(list_persons, key=lambda item: item.age)

	print('Oldest person - Name: {}, Surname: {}, Age: {}'.format(max_person_age.name, max_person_age.surname, max_person_age.age))
	print('Yongest person - Name: {}, Surname: {}, Age: {}'.format(min_person_age.name, min_person_age.surname, min_person_age.age))



if __name__ == "__main__":
	main()
