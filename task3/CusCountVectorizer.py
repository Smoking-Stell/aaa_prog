import string


class CusCountVectorizer:
    def __init__(self, vocabulary: dict = None):
        if vocabulary is None:
            self.vocabulary_ = {}
        else:
            self.vocabulary_ = vocabulary

    @staticmethod
    def _preprocess(text):
        return text.lower().translate(
            str.maketrans('', '', string.punctuation))

    def fit(self, documents):
        word_id = 0
        for doc in documents:
            for word in doc.split():
                word = self._preprocess(word)
                if word not in self.vocabulary_:
                    self.vocabulary_[word] = word_id
                    word_id += 1
        return self

    def transform(self, documents):
        vectors = []
        for doc in documents:
            vector = [0] * len(self.vocabulary_)
            for word in doc.split():
                word = self._preprocess(word)
                if word in self.vocabulary_:
                    vector[self.vocabulary_[word]] += 1
            vectors.append(vector)
        return vectors

    def fit_transform(self, documents):
        self.fit(documents)
        return self.transform(documents)

    def get_feature_names_out(self):
        return sorted(self.vocabulary_, key=self.vocabulary_.get)

    def get_feature_names(self):
        return self.get_feature_names_out()
