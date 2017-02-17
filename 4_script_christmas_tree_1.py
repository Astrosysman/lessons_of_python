#!/usr/bin/env python3

limit = 10

for k in range(7, limit, 1):
	for i in range(k, 1, -1):
	    print (( i + ( limit - k )) * ' ' + 2 * ( k + 1 - i ) * '*' + i * ' ')

