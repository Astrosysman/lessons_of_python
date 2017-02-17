#!/usr/bin/env python3

limit = 10


for j in range(limit):
    for i in range(limit):
        if limit - j <= i:
            print("* ", end='')
        else:
            print(" ", end='')
    print()

for j in range(limit):
    for i in range(limit):
        if j <= i:
            print("* ", end='')
        else:
            print(" ", end='')
    print()

