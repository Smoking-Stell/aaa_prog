import pytest

from one_hot_encoder import fit_transform


def test_empty_input():
    with pytest.raises(TypeError):
        fit_transform()


def test_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]

    assert fit_transform(cities) == exp_transformed_cities


def test_onlyone():
    input_data = ['Moscow', 'Moscow', 'Moscow']
    output = fit_transform(input_data)
    vectors = [x for x in output]
    assert all(x == vectors[0] for x in vectors)


def test_onlyone_withstar():
    input_data = ['Moscow', 'Moscow', 'Moscow']
    output = fit_transform(*input_data)
    vectors = [x for x in output]
    assert all(x == vectors[0] for x in vectors)


def test_hard():
    cities = ['London', 'New York', 'London', 'Moscow',
              'New York', 'Moscow', 'London']

    transformed = fit_transform(cities)

    city_vectors = {}

    for (city, vector) in transformed:
        if city not in city_vectors:
            city_vectors[city] = vector
        else:
            assert city_vectors[city] == vector, \
                f"Vector for city '{city}' not equal."

    assert len(city_vectors.values()) == len(set(cities)), \
        "Number of unique cities incorrect"
