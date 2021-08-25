name = input()

if len(name) > 5 and len(name) < 10:
    print(name)
    print("Hej på dig")
    if name == "Hampus":
        print("Så fint namn")
    print("Hej då")
else:
    print("Dålig längd du...")
