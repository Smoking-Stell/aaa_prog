from task3.CusCountVectorizer import CusCountVectorizer
from task4.TfidfTransformer import TfidfTransformer


class TfidfVectorizer(CusCountVectorizer):
    """Inherited from CusCountVectorizer
        Added tdidf calculation method

    """

    def __init__(self):
        """class initialization

        """
        super().__init__()
        self.tfidf_ = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self.tfidf_.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print("Tfidf with vectorizer test: ")
    for i in tfidf_matrix:
        print(i)
