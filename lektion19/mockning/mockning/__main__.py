import mockning.base.joker as joker

j = joker.Joker()
joke_list = j.jokes(3)

for joke in joke_list:
    print(joke)
