from task4.TransformFunctions import tf_transform, idf_transform


class TfidfTransformer:
    def fit_transform(self, count_matrix: list) -> list:
        """Calculate tfidf matrix for each document

        :param count_matrix: matrix which shows amount of words
        from documents; each row is doc, each column is word
        :return: tfidf matrix
        """
        tfs = tf_transform(count_matrix)
        idfs = idf_transform(count_matrix)
        res = []
        for doc in tfs:
            res.append([round(t * i, 3) for t, i in zip(doc, idfs)])
        return res


if __name__ == '__main__':
    count_matrix_test = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix_test)
    print("Tfidf test: ")
    for i in tfidf_matrix:
        print(i)