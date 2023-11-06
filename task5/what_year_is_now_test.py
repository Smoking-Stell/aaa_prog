import unittest
from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_ymd(self, mock_urlopen):
        """testing YYYY-MM-DD

        :param mock_urlopen:
        :return:
        """
        mock_response = MagicMock()
        mock_response.__enter__.return_value.read.return_value =\
            '{"currentDateTime": "2019-11-06"}'
        mock_urlopen.return_value = mock_response

        year = what_is_year_now()

        self.assertEqual(year, 2019)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_dmy(self, mock_urlopen):
        """testing DD-MM-YYYY

        :param mock_urlopen:
        :return:
        """
        mock_response = MagicMock()
        mock_response.__enter__.return_value.read.return_value =\
            '{"currentDateTime": "19.08.2002"}'
        mock_urlopen.return_value = mock_response

        year = what_is_year_now()

        self.assertEqual(year, 2002)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_invalid(self, mock_urlopen):
        """testing wrong format

        :param mock_urlopen:
        :return:
        """
        mock_response = MagicMock()
        mock_response.__enter__.return_value.read.return_value =\
            '{"currentDateTime": "2002/05/06"}'
        mock_urlopen.return_value = mock_response

        with self.assertRaises(ValueError):
            what_is_year_now()

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_invalid2(self, mock_urlopen):
        """testing wrong year

        :param mock_urlopen:
        :return:
        """
        mock_response = MagicMock()
        mock_response.__enter__.return_value.read.return_value = \
            '{"currentDateTime": "988-05-06"}'
        mock_urlopen.return_value = mock_response

        with self.assertRaises(ValueError):
            what_is_year_now()
