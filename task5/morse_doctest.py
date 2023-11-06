import doctest


LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """Encodes a string according to the Morse code table

    :param message: string we need to code
    :return: morse string
    >>> encode("АПР") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    KeyError: 'А'
    >>> encode("SOS") # doctest: +NORMALIZE_WHITESPACE
    '... --- ...'
    >>> encode("467") # doctest: +NORMALIZE_WHITESPACE
    '....- -.... --...'
    >>> encode("BERLIN") # doctest: +NORMALIZE_WHITESPACE
    '-... . .-. .-.. .. -.'
    >>> encode("SPB") # doctest: +NORMALIZE_WHITESPACE
    '... .--. -...'
    >>> encode("QUICK") # doctest: +NORMALIZE_WHITESPACE
    '--.- ..- .. -.-. -.-'
    >>> encode("1  2 9") # doctest: +NORMALIZE_WHITESPACE
    '.---- ..--- ----.'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Decode a string according to the Morse code table
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


if __name__ == '__main__':
    doctest.testmod()
    morse_msg = '-- .- .. -....- .--. -.-- - .... --- -. -....- ' \
                '..--- ----- .---- ----.'
    decoded_msg = decode(morse_msg)
    print(decoded_msg)
    assert morse_msg == encode(decoded_msg)
