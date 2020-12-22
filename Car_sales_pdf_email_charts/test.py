#!/usr/bin/env python3

a = [10, 11, 12, 13, 14]
b = [10, 11, 12, 13, 14]
c = []
for i in range(len(a)):
    x = a[i] * b[i]
    c.append(x)

print(c)
