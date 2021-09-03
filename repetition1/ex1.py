str_to_num = {
    "noll": 0,
    "ett": 1,
    "två": 2,
    "tre": 3,
    "fyra": 4,
    "fem": 5,
    "sex": 6,
    "sju": 7,
    "åtta": 8,
    "nio": 9
}

def print_answer(num_cars):
    if num_cars < 0:
        print("Det antalet bilar kan vi inte ha, fåntratt!")
    elif num_cars > 4:
        print("Du har många bilar")
    elif num_cars > 0:
        print("Ok, det var några bilar")
    else:
        print("Ok, man behöver inte någon bil.")

def string_to_number(s):
    """Convert a number (as a string) in swedish to an integer"""
    s = s.lower()
    if s in str_to_num:
        return str_to_num[s]
    else:
        raise ValueError(f"{s} är inte ett tal")

def read_cars():
    print("Hur många bilar äger du?")
    num_cars = input()

    if not num_cars.isnumeric():
        return string_to_number(num_cars)
    else:
        return int(num_cars)

try:
    num = read_cars()
    print_answer(num)
except ValueError:
    print("Du skrev inte ett tal!")
