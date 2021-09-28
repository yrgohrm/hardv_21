import mockning.net.dadapi as dadapi
import unittest
from unittest.mock import patch, MagicMock


class TestDadService(unittest.TestCase):
    def test_get_joke(self):
        """Test getting a single joke"""

        default_joke = "hahaha"

        with patch("urllib.request.urlopen") as mock:
            resp = MagicMock()
            resp.read.return_value = f'{{"joke":"{default_joke}"}}'
            mock.return_value = resp

            ds = dadapi.DadService()
            joke = ds.joke()

            resp.read.assert_called_once_with()
            self.assertEqual(joke, default_joke)
