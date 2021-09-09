import random

# with open("jokes.txt", "r", encoding="UTF-8") as file:
#     jokes = file.readlines()
#     random_number = random.randrange(0, len(jokes))
#     print(jokes[random_number])

with open("jokes.txt", "w", encoding="UTF-8") as file:
    jokes = file.readlines()
    print(random.choice(jokes))

