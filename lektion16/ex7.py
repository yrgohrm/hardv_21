my_str = "Hejsan hoppsan. Vem är du? öh?"
the_bytes = bytearray(my_str, "UTF-8")
my_other_str = the_bytes.decode("UTF-8")

print(my_str)
print(my_other_str)
