from . import probability
from . import board


def generate_space_on_board():
    return generate_room(), generate_space_in_room()


def generate_room():
    return probability.generate_from_relative_probability({x: 1 for x in board.rooms})


def generate_space_in_room():
    return probability.roll_d10()


def generate_item():
    """Pull an item out of a bag w/ replacement"""

    return probability.generate_from_relative_probability({
        "electronics": 1,
        "food": 0,
        "knickknacks": 1,
        "string": 1,
        "toy": 1,
    })

