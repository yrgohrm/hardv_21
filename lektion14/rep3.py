def get_name():
    return input("Vad heter du? ")

def get_age():
    while True:
        try:
            return int(input("Hur gammal är du? "))
        except ValueError:
            print("Skriv in ett heltal tack!")

name = get_name()
age = get_age()

if age < 18:
    print(f"Tjena {name}")
else:
    print(f"Goddag {name}")
