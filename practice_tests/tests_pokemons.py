import doctest

class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
    def __str__(self) -> str:
        """Return string representation of a Pokemon.

        >>> str(Pokemon("Bulbasaur", "grass"))
        'Bulbasaur/grass'
        >>> str(Pokemon("Pikachu", "electric\\r\\npower"))
        'Pikachu/electric\\r\\npower'
        >>> str(Pokemon("Squirtle", "water" * 30))
        'Squirtle/waterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwaterwater'

        :return:
        """
        return f'{self.name}/{self.poketype}'


def test_assert_str():
    name = "Bulbasaur"
    poketype = "grass"
    assert str(Pokemon(name, poketype)) == "Bulbasaur/grass"

    name = "Pickachu"
    poketype = "electric\r\npower"
    assert str(Pokemon(name, poketype)) == "Pickachu/electric\r\npower"

    name = 'Squirtle'
    poketype = 'water' * 30
    waters = ""
    for i in range(30):
        waters += "water"
    assert str(Pokemon(name, poketype)) == "Squirtle/" + waters

    # try:
    # except AssertionError:
    #     pass


if __name__ == "__main__":
    doctest.testmod()
    test_assert_str()


