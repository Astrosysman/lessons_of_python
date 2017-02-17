#!/usr/bin/env python3

limit = 10

for j in range(limit):
    print('* ' * (limit - j))

print("",end="\n\n")

for j in range(limit + 1):
    print('* ' * j)

print("",end="\n\n")

for j in range(limit):
    for i in range(limit):
        if limit -1 - j > i:
            print("  ", end='')
        else:
            print("* ", end='')
    print()

print("",end="\n\n")

for j in range(limit):
    for i in range(limit):
        if limit -1 - j < i:
            print("  ", end='')
        else:
            print("* ", end='')
    print()

print("",end="\n\n")

for j in range(limit):
    for i in range(limit):
        if j <= i:
            print("* ", end='')
        else:
            print(" ", end='')
    print()

print("",end="\n\n")


for j in range(limit):
    for i in range(limit):
        if limit - j <= i:
            print("* ", end='')
        else:
            print(" ", end='')
    print()
