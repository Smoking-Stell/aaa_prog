class MainPizza:
    def __init__(self, size: str = "XL"):
        self.size = size
        self.recipe = {}
        self.status = "preparing"

    def dict(self) -> dict:
        """give recipe in dict presentation

        :return: dict
        """
        return self.recipe

    def __eq__(self, other) -> bool:
        """compare two pizza objects
        if recipes and sizes are equal then pizzas are equal

        :param other: other instance
        :return: True or False
        """
        if not isinstance(other, MainPizza):
            return NotImplemented
        return self.size == other.size and self.recipe == other.dict()

    def set_status(self, new_status: str) -> None:
        """
        Set new pizza status

        :return:
        """
        self.status = new_status

    def __str__(self) -> str:
        return "Pizza"


class Pepperoni(MainPizza):
    def __init__(self, size: str = "XL"):
        super().__init__(size)
        self.recipe.update({
            'tomato sauce': '100g',
            'mozzarella': '200g',
            'peperoni': '150g'
        })

    def __str__(self) -> str:
        return "Pepperoni"


class Margherita(MainPizza):
    def __init__(self, size: str = "XL"):
        super().__init__(size)
        self.recipe.update({
            'tomato sauce': '100g',
            'mozzarella': '200g',
            'tomatoes': '150g'
        })

    def __str__(self) -> str:
        return "Margherita"


class Hawaiian(MainPizza):
    def __init__(self, size: str = "XL"):
        super().__init__(size)
        self.recipe.update({
            'tomato sauce': '100g',
            'mozzarella': '200g',
            'chicken': '150g',
            'pineapples': '50g'
        })

    def __str__(self) -> str:
        return "Hawaiian"
