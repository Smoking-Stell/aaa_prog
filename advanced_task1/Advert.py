import json
import keyword


def is_keyword(word):
    keyword_list = keyword.kwlist

    if word in keyword_list:
        return True
    else:
        return False


class ColorizeMixin:
    repr_color_code = 0

    def __str__(self):
        original_str = super().__str__()
        return f"\033[{self.repr_color_code}m{original_str}\033[0m"



class Advert(ColorizeMixin):

    def __init__(self, mapping):
        if isinstance(mapping, str):
            mapping = json.loads(mapping)
        self.price_ = 0

        for key, value in mapping.items():
            if isinstance(value, dict):
                value = Advert(value)
            if key == "price":
                self.price = value
            if is_keyword(key):
                key += '_'
            setattr(self, key, value)

    def __str__(self):
        attributes = vars(self)

        attributes_str_list = []

        for key, value in attributes.items():
            attributes_str_list.append(f"{value}")
        return "| ".join(attributes_str_list)

    @property
    def price(self):
        return self.price_

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be number")
        if value < 0:
            raise ValueError("Price must be >= 0")
        self.price_ = value


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

    ad.price = 150
    print(ad.price)

    try:
        ad2 = {"price": 100,
               "color": "green"}
    except ValueError as e:
        print(e)


    ad3 = Advert({  "title": "Вельш-корги",
                "price": 1000,
                "class": "dogs",
                "location": {
                    "address": "сельское поселение Ельдигинское, "
                           "поселок санатория Тишково, 25"
                }
            })


    print(ad3)


if __name__ == '__main__':
    main()