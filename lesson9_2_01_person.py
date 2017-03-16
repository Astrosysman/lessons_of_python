#!/usr/bin/env python3

class Person:
	def __init__(self, name, surname, age):
		self.name = name
		self.surname = surname
		self.age = age

	def __str__(self):
		return 'Name: ' + self.name + '\nSurname: ' + self.surname + '\nAge: ' + str(self.age) + '\n'


