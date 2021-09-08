with open("test2.txt", "rb") as file:
    data = file.read(2)
    print(data[0])
    print(data[1])
    print(data)
    print(len(data))