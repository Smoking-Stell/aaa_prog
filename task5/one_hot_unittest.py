import unittest

from one_hot_encoder import fit_transform

class TestOneHot(unittest.TestCase):
    def test_solo(self):
        self.assertEqual(fit_transform('apple'), [('apple', [1])])

    def test_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_notzeros(self):
        """we can't have 0,0,0 vector

        :return:
        """
        fruits = ('apple', 'orange', 'banana')
        output = fit_transform(fruits)
        self.assertNotIn([0, 0, 0], [x[1] for x in output])

    def test_onlyone(self):
        city = ["Moscow", "Moscow", "Moscow"]
        expected = [
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1])
        ]
        self.assertEqual(fit_transform(city), expected)


    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()


