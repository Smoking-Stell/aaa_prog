import string


class CusCountVectorizer:
    def __init__(self, vocabulary: dict = None):
        """Initialization of vocabulary for class

        :param vocabulary: if given make the vocabulary
        """
        if vocabulary is None:
            self.vocabulary_ = {}
        else:
            self.vocabulary_ = vocabulary

    @staticmethod
    def _preprocess(text: string) -> string:
        """Format string to lower case and delete punctuation symbols

        :param text: unformatted string
        :return: formatted string
        """
        return text.lower().translate(
            str.maketrans('', '', string.punctuation))

    def fit(self, documents: list):
        """Find all unique words in documents and fill the vocabulary
        in order of receiving words: word is key, and it's number is value

        :param documents: list of texts where we need to find all unique words
        :return: CusCountVectorizer
        """
        word_id = 0
        for doc in documents:
            for word in doc.split():
                word = self._preprocess(word)
                if word not in self.vocabulary_:
                    self.vocabulary_[word] = word_id
                    word_id += 1
        return self

    def transform(self, documents: list) -> list:
        """Matches words with words in the dictionary and make a vector
        of words amounts for each document.
        Indexes of vector are from vocabulary

        :param documents: list of documents where we need
         to find amount of words
        :return: list of vectors for documents
        """
        vectors = []
        for doc in documents:
            vector = [0] * len(self.vocabulary_)
            for word in doc.split():
                word = self._preprocess(word)
                if word in self.vocabulary_:
                    vector[self.vocabulary_[word]] += 1
            vectors.append(vector)
        return vectors

    def fit_transform(self, documents: list) -> list:
        """Combine fit and transform

        :param documents: list of documents where we need
         to find amount of words after making a vocabulary
        :return: list of vectors for documents
        """
        self.fit(documents)
        return self.transform(documents)

    def get_feature_names_out(self) -> list:
        """ Make an ordered sequence of words for the vocabulary.
        Order of receiving

        :return: list of words from the vocabulary
        """
        return sorted(self.vocabulary_, key=self.vocabulary_.get)

    def get_feature_names(self):
        """Old version of get_feature_names_out

        :return:
        """
        return self.get_feature_names_out()
