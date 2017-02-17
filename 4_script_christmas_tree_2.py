#!/usr/bin/env python3

limit = 10

for k in range(limit, 7, -1):
	for i in range(1, k, 1):
	    print (( i + ( limit - k )) * ' ' + 2 * ( k - i ) * '*' + i * ' ')

