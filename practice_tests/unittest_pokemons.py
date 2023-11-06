import unittest
from tests_pokemons import Pokemon

class TestPokemonStrMethod(unittest.TestCase):

    def test_bulbasaur(self):
        pokemon = Pokemon("Bulbasaur", "grass")
        self.assertEqual(str(pokemon), "Bulbasaur/grass")

    def test_pikachu(self):
        pokemon = Pokemon("Pikachu", "electric\r\npower")
        self.assertEqual(str(pokemon), "Pikachu/electric\r\npower")

    def test_squirtle(self):
        poketype = 'water' * 30
        pokemon = Pokemon('Squirtle', poketype)
        self.assertEqual(str(pokemon), "Squirtle/" + poketype)


if __name__ == '__main__':
    unittest.main()
