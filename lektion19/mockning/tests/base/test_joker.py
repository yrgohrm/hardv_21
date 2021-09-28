from mockning.base import joker
from unittest.mock import patch
import unittest


class TestJoker(unittest.TestCase):
    def test_get_default(self):
        default_joke = "hahaha"
        with patch("mockning.net.dadapi.DadService") as mock:
            instance = mock.return_value
            instance.joke.return_value = default_joke

            joker_instance = joker.Joker()
            jokes = joker_instance.jokes()

            instance.joke.assert_called_once_with()
            self.assertListEqual(jokes, [default_joke])
