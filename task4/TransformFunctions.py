import math


def tf_transform(count_matrix: list) -> list:
    """ Calculate tf vectors (repetitions / total) for each document in matrix

    :param count_matrix: matrix which shows amount of words
     from documents; each row is doc, each column is word
    :return: tf matrix
    """
    tf_matrix = [[0] * len(count_matrix[0]) for _ in
                 range(len(count_matrix))]

    for i, row in enumerate(count_matrix):
        words_sum = 0
        for x in row:
            words_sum += x
        for j, x in enumerate(row):
            tf_matrix[i][j] = round(x / words_sum, 3)
    return tf_matrix


def idf_transform(count_matrix: list) -> list:
    """ Calculate idf vector (ln ((total documents + 1)/
                                    (documents with words + 1)) + 1)
    for each word in matrix

    :param count_matrix: matrix which shows amount of words
     from documents; each row is doc, each column is word
    :return: idf vector
    """

    total_docs = len(count_matrix)
    total_words = len(count_matrix[0])
    idf_values = []

    for i in range(total_words):
        docs_i = 0
        for doc in count_matrix:
            if doc[i] > 0:
                docs_i += 1
        idf_val = math.log((total_docs + 1) / (docs_i + 1)) + 1
        idf_values.append(round(idf_val, 3))
    return idf_values


if __name__ == '__main__':
    count_matrix_test = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    print(f"TF test: {tf_transform(count_matrix_test)}\n")
    print(f"IDF test: {idf_transform(count_matrix_test)}\n")
