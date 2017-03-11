#!/usr/bin/env python3

class ExceptionLicense(Exception):
	pass

class Editor:
	def edit_document(self):
		self.edit_text = 'Editing of documents is not available in the free version'
		return self.edit_text

	def view_document(self):
		self.view_text = 'You can view documents'
		return self.view_text
		

class ProEditor(Editor):

	def edit_document(self):
		super().edit_document()
		self.edit_text = 'In the pro version you can edit the documents'
		return self.edit_text

def check_license(key_license):

	key = 'Hds/Fl84EllMMh3j'
	try:
		if key != key_license:
			raise ExceptionLicense
	except ExceptionLicense:

		user_access_editor = Editor()
		return user_access_editor.edit_document(), user_access_editor.view_document()
	else:
		user_access_proeditor = ProEditor()
		return user_access_proeditor.edit_document(), user_access_proeditor.view_document()
			

def main():
	print(check_license(input('Enter key license: ')))

if __name__ == "__main__":
	main()
