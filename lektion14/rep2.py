def divide(a, b):
    if b == 0:
        raise ValueError("ajabaja inte dela med noll!")
    return a / b

def do_some_division(val):
    a = divide(val, 3)
    b = divide(val, a+1)
    return divide(b, val)

try:
    print(do_some_division(0))
    print(do_some_division(0))
    print(do_some_division(0))
    print(do_some_division(0))
    print(do_some_division(0))
    print(do_some_division(0))
    print(do_some_division(0))
    print(do_some_division(0))
    print(do_some_division(0))
except ValueError:
    print("Det blev fel")

print("Klart!")