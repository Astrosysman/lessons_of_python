#!/usr/bin/env python3

limit = 11

for j in range(limit):

	bini = j%2
	step = j + bini

	print('{}{}'.format('  '* step, '* '))

	if bini == 0:

		print('{}{}'.format('  '* step, '* ' * 3))


