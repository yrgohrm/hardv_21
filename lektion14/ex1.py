def do_stuff():
    return ("Hej", 22)


val, count = do_stuff()

print(val)
print(count)

# "gammla" sättet, inte så tydligt
ret_val = do_stuff()

print(ret_val[0])
print(ret_val[1])
