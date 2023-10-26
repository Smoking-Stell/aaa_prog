import math


class TfidfTransformer:
    @staticmethod
    def tf_transform(count_matrix):
        tf_matrix = [[0] * len(count_matrix[0]) for _ in
                     range(len(count_matrix))]

        for i, row in enumerate(count_matrix):
            words_sum = 0
            for x in row:
                words_sum += x
            for j, x in enumerate(row):
                tf_matrix[i][j] = round(x / words_sum, 3)
        return tf_matrix

    @staticmethod
    def idf_transform(count_matrix):
        """

        :param count_matrix: matrix which shows presents of words
         from documents; each row is doc, each column is word
        :return: idf
        """
        # check_matrix = (np.array(count_matrix).astype(bool))
        # doc_count_per_word = check_matrix.sum(axis=0)
        # idf_values = np.log((len(count_matrix) + 1)/(1 + doc_count_per_word))

        idf_values = []
        total_docs = len(count_matrix)
        total_words = len(count_matrix[0])
        for i in range(total_words):
            docs_i = 0
            for doc in count_matrix:
                if doc[i] > 0:
                    docs_i += 1
            idf_values.append(
                round(math.log((total_docs + 1) / (docs_i + 1)) + 1, 3))
        return idf_values

    def fit_transform(self, count_matrix):
        tfs = self.tf_transform(count_matrix)
        idfs = self.idf_transform(count_matrix)
        res = []
        for doc in tfs:
            res.append([round(t * i, 3) for t, i in zip(doc, idfs)])
        return res


if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
                    ]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)
