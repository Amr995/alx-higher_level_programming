#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisoinError):
        print("Inside result: {:d}",div = None)
        return None
    finally:
        print("Inside result: {:d}",div)
        return div
