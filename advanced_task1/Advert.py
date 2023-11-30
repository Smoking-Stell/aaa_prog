import json
import keyword


def is_keyword(word):
    keyword_list = keyword.kwlist

    if word in keyword_list:
        return True
    else:
        return False


class Advert:

    def __init__(self, mapping):
        if isinstance(mapping, str):
            mapping = json.loads(mapping)
        self.price = 0

        for key, value in mapping.items():
            if isinstance(value, dict):
                value = Advert(value)
            if key == "price":
                self.price = value
            if is_keyword(key):
                key += '_'
            setattr(self, key, value)

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be number")
        if value < 0:
            raise ValueError("Price must be >= 0")
        self._price = value


def main():
    json_test = """{
                "title": "iPhone X",
                "price": 100,
                "location": {
                        "address": "город Самара, улица Мориса Тореза, 50",
                        "metro_stations": ["Спортивная", "Гагаринская"]
                        }
            }"""

    ad = Advert(json.loads(json_test))
    print(ad.location.metro_stations)


if __name__ == '__main__':
    main()