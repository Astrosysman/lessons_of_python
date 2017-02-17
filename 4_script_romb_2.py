#!/usr/bin/env python3

limit = 10

my_range = list(range(limit, 1, -1)) + list(range(1, limit + 1))
for i in my_range:
    print (' ' * i +  '*' * ( limit - i ) * 2 + ' ' * i )
