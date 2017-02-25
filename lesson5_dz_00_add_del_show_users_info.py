#!/usr/bin/env python3

#Программа формирует базу пользовательской информации(username, password, email),
#позволяя добавлять, удалять и смотреть содержимое это базы
#Автор Вазинский Виталий

storage = [
	{'email': 'qwer@com', 'password': 'qwer', 'username': 'qwer'},
	{'email': '123@com', 'password': '123', 'username': '123'},

]

def add(users_info):
	user = {}
	user['username'] = input('Enter username: ')	
	user['password'] = input('Enter user password: ')	
	user['email'] = input('Enter user email: ')	

	users_info.append(user)

	print('{} {} {}'.format("User", user['username'] ,"information is added"))

def del_(users_info):

	username_ = input('Enter username: ')	

	for i in range(len(users_info)):
		if users_info[i]['username'] == username_:
			del users_info[i]
			return print('{} {} {}'.format("User", username_, "was deleted"))

	print('{} {} {}'.format("User", username_, "is not exist"))
			
		

def show(users_info):
	for i in range(len(users_info)):
		print()
		print('{}: {}'.format('Username',users_info[i]['username']))
		print('{}: {}'.format('Password',users_info[i]['password']))
		print('{}: {}'.format('Email',users_info[i]['email']))


def main():

	repeat_ = 'y'
	while repeat_ != 'n' :

		your_choise = input('Enter your operation - add, del, show: ')

		operation = {

			'add': add,
			'del': del_,
			'show': show ,

		}

		if your_choise in operation.keys():
			operation[your_choise](storage)
		else:
			print('No such operation')

		repeat_ = input('Repeat the operation("y" or "n", default "y"): ')

main()
