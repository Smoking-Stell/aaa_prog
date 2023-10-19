class CountVectorizer:
    def __init__(self):
        self.vocabulary_ = {}

    def fit(self, documents):
        word_id = 0
        for doc in documents:
            for word in doc.split():
                word = word.lower()
                if word not in self.vocabulary_:
                    self.vocabulary_[word] = word_id
                    word_id += 1
        return self
