my_list = [ x * x for x in range(1, 5) ]
print(my_list)

temp = []
for x in range(1, 5):
    temp.append(x * x)
my_list = temp

print(my_list)
