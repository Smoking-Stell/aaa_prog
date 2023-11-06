import pytest

from morse import decode

test_data = [
        ('--.- ..- .. -.-. -.-', 'QUICK'),
        ('-- --- .-. ... .', 'MORSE'),
        ('... --- ...', 'SOS'),
        ('.---- ..--- ----.', '129'),
    ]


@pytest.mark.parametrize("morse_message, expected", test_data)
def test_decode(morse_message, expected):
    assert decode(morse_message) == expected
