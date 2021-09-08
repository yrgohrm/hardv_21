with open("test2.txt", "rb") as file:
    data = file.read(100)
    print(data)
    print(len(data))