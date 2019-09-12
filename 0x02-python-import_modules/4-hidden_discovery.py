#!/usr/bin/python3
import hidden_4
for i in dir(hidden_4):
    if "__" in i:
        continue
    else:
        print(i)
