#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(input("Enter a number: "))
    except valueError:
        return False
    else:
        return True
