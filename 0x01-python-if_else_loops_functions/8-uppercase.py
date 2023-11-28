#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            print(f'{uppercase_char}', end='')
        else:
            print(f'{char}', end='')
    print()
