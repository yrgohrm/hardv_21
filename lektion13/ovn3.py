mile = 1.609
gallon = 3.785

print("Hur många mpg?")
mpg = float(input())

# Dålig kod!! Vad är 23.521!?
lpm = 23.521 / mpg

print(f"liter per mil = {lpm:.2f}")
