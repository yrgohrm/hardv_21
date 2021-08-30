def get_numbers():
    """Reads a list of numbers from the terminal and returns them as a list"""
    list_of_numbers = []
    print("Skriv in ett nummer per rad. Avsluta med tomrad.")
    while True:
        try:
            line = input()
            if len(line) == 0:
                break
            number = int(line)
            list_of_numbers.append(number)
        except ValueError:
            print("Snälla skriv in ett tal!")
    return list_of_numbers

def prod(values):
    res = values[0]
    for x in values[1:]:
        res *= x
    return res

some_list_of_numbers = get_numbers()

if len(some_list_of_numbers) > 0:
    the_sum = sum(some_list_of_numbers)
    the_avg = the_sum / len(some_list_of_numbers)
    the_prod = prod(some_list_of_numbers)

    print(f"Summan är {the_sum}")
    print(f"Medel är {the_avg}")
    print(f"Produkten är {the_prod}")
else:
    print("No numbers entered")