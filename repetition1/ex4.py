# spelare name, email, latest score, high score

class Player:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__latest_score = 0
        self.__high_score = 0

    def set_last_score(self, score):
        self.__latest_score = score
        if score > self.__high_score:
            self.__high_score = score

    def get_email(self):
        return self.__email

    def get_name(self):
        return self.__name

    def __eq__(self, other):
        return self.__name == other.__name and self.__email == other.__email

    def __repr__(self):
        return f"Player({self.__name}, {self.__email}, {self.__latest_score}, {self.__high_score})"


some_player = Player("Bosse", "bosse@bredsladd.se")
some_player.set_last_score(100)
some_player.set_last_score(10)
some_player.set_last_score(99)

print(f"Spelare: {some_player}")