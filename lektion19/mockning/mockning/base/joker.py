import mockning.net.dadapi as dadapi


class Joker:
    def __init__(self):
        self.__dad_service = dadapi.DadService()
        self._joke_list = []

    def jokes(self, num=1):
        if len(self._joke_list) < num:
            self.__fill_to(num)
        return self._joke_list[:num]

    def __fill_to(self, num):
        while (num - len(self._joke_list)) > 0:
            joke = self.__dad_service.joke()
            self._joke_list.append(joke)
