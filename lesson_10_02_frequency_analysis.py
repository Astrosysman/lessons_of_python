#!/usr/bin/env python3

# Программа выводит слово, наиболее часто встречающееся в файле text
# Автор Вазинский Виталий

def open_file():

	words = []

	with  open('text', 'r') as text:

		for line in text:
			for word in line.split():
				words.append(word)

	return words

def frequency_of_words(words):

	words_freq = {}

	for word in words:
		if word in words_freq:
			freq = words_freq[word]
			words_freq[word] = freq + 1
		else:
			words_freq[word] = 1

	return words_freq

def main():

	words_freq = frequency_of_words(open_file())

	max_freq = max(words_freq, key=lambda item: int(words_freq[item]))

	print(max_freq)

if __name__ == '__main__':
	main()
