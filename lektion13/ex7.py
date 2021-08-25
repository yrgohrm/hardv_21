def doerror(value):
    print("Hej")

    if value < 0:
        raise ValueError("value is less than zero")

def apa():
    try:
        doerror(-12)
    except ValueError:
        print("Det blev ValueError")

apa()
