import pytest

from pizza_delivery import order, menu
from Pizzas import Pepperoni, Margherita, MainPizza


def test_menu(capsys):
    """
    Testing menu func
    :return:
    """

    try:
        menu()
    except SystemExit as e:
        pass
    captured = capsys.readouterr()

    assert "Margherita" in captured.out
    assert "Hawaiian" in captured.out
    assert "Pepperoni" in captured.out
    assert "tomato sauce" in captured.out
    assert "pork" not in captured.out


def test_pizzas():
    peper = Pepperoni("XL")
    peper2 = Pepperoni("L")

    mar = Margherita("L")
    mar2 = Margherita("L")

    def_pizza = MainPizza()

    assert peper != peper2
    assert mar == mar2
    assert mar != peper2
    assert def_pizza != mar

