import unittest

from task3.CusCountVectorizer import CusCountVectorizer


class TestCustomCountVectorizer(unittest.TestCase):

    def setUp(self):
        self.vectorizer = CusCountVectorizer()

    def test_fit(self):
        self.vectorizer = CusCountVectorizer()
        docs = ["Hello world", "World hello"]
        self.vectorizer.fit(docs)
        expected_vocab = {'hello': 0, 'world': 1}
        self.assertEqual(self.vectorizer.vocabulary_, expected_vocab)

    def test_transform(self):
        self.vectorizer = CusCountVectorizer()
        docs = ["Привет мир", "Мир привет"]
        self.vectorizer.fit(docs)
        vectors = self.vectorizer.transform(docs)
        expected_vectors = [[1, 1], [1, 1]]
        self.assertEqual(vectors, expected_vectors)

    def test_fit_transform(self):
        self.vectorizer = CusCountVectorizer()
        docs = ["Привет мир", "Мир привет"]
        vectors = self.vectorizer.fit_transform(docs)
        expected_vectors = [[1, 1], [1, 1]]
        self.assertEqual(vectors, expected_vectors)

    def test_fit_transform2(self):
        self.vectorizer = CusCountVectorizer()
        docs = ["привет, пока! ::привет,",
                "Привет ;пока здравствуйте; салют салют"]
        vectors = self.vectorizer.fit_transform(docs)
        expected_vectors = [[2, 1, 0, 0], [1, 1, 1, 2]]
        self.assertEqual(vectors, expected_vectors)

    def test_get_feature_names(self):
        self.vectorizer = CusCountVectorizer()
        docs = ["здравствуйте, ДОРОГОЙ: ;,Мартин", "поехали, туда"]
        self.vectorizer.fit(docs)
        feature_names = self.vectorizer.get_feature_names()
        expected_names = ['здравствуйте', 'дорогой',
                          "мартин", "поехали", "туда"]
        self.assertEqual(feature_names, expected_names)

    def test_fit_transform3(self):
        docs = [
            "Crock Pot Pasta Never boil pasta again",
            "Pasta Pomodoro Fresh ingredients Parmesan to taste"
        ]
        vectors = self.vectorizer.fit_transform(docs)

        expected_vectors = [
            [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(vectors, expected_vectors)

    def test_get_feature_names3(self):
        docs = [
            "Crock Pot Pasta Never boil pasta again",
            "Pasta Pomodoro Fresh ingredients Parmesan to taste"
        ]
        self.vectorizer.fit(docs)
        feature_names = self.vectorizer.get_feature_names()

        expected_names = ['crock', 'pot', 'pasta', 'never', 'boil', 'again',
                          'pomodoro', 'fresh', 'ingredients',
                          'parmesan', 'to', 'taste']
        self.assertEqual(feature_names, expected_names)


if __name__ == '__main__':
    unittest.main()
