from random import randint

import click

from Pizzas import Pepperoni, Hawaiian, Margherita, MainPizza

pizza_menu = {
    "margherita": Margherita,
    "pepperoni": Pepperoni,
    "hawaiian": Hawaiian,
}


@click.group()
def cli():
    pass


def log(template):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            duration = randint(1, 100)
            print(template.format(int(duration)))
            return result
        return wrapper
    return decorator


@log('Доставили за {}с!')
def deliver(pizza: MainPizza) -> None:
    """Deliver pizza

    :param pizza:
    :return:
    """
    pizza.set_status("delivered")


@log('Приготовили за {}с!')
def bake(pizza: MainPizza) -> None:
    """Bake pizza

    :param pizza:
    :return:
    """
    pizza.set_status("baked")


@log('Забрали за {}с!')
def pick_up(pizza: MainPizza) -> None:
    """Customer pick up pizza

    :param pizza:
    :return:
    """

    pizza.set_status("delivered")


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(pizza: str, size: str, delivery: bool):
    """
    Заказывает пиццу


    Order for pizza, which create new

    :param pizza: type of pizza
    :param size: size of pizza
    :param delivery: is delivery needed
    :return:
    """

    current_pizza = pizza_menu[pizza](size)
    bake(current_pizza)

    if delivery:
        deliver(current_pizza)
    else:
        pick_up(current_pizza)
    pass


@cli.command()
def menu():
    """
    Выводит меню
    """

    all_pizzas = MainPizza.__subclasses__()
    for pizza_class in all_pizzas:
        pizza_instance = pizza_class()
        ingridients = ', '.join(pizza_instance.dict().keys())
        print(f'- {str(pizza_instance)} : {ingridients}')


cli.add_command(order)
cli.add_command(menu)

if __name__ == '__main__':
    cli()
