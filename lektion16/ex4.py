with open("test.txt", "r") as file:
    for line in file:
        print("en rad:", line)

with open("test.txt", "r") as file:
    all_data = file.read()
    print(all_data)

with open("test.txt", "r") as file:
    all_data = file.readlines()
    print(all_data)
