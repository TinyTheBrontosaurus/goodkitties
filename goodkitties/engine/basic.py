import networkx as nx
import natsort
import matplotlib.pyplot as plt
import math
import random


def main(_argv):
    # Auto render the board
    _ = plt.subplot(1, 1, 1)
    nx.draw_spring(board_v2(), with_labels=True, font_weight='bold')
    plt.show()

def generate_space_on_board():
    return generate_room(), generate_space_in_room()


def generate_room():
    return generate_from_relative_probability({x: 1 for x in rooms})


def generate_space_in_room():
    return roll_d10()


def roll_d10():
    return roll_d(10)


def roll_d6():
    return roll_d(6)


def roll_d(sides: int):
    val = random.uniform(sides)
    return int(math.floor(val))


def generate_item():

    return generate_from_relative_probability({
        "electronics": 1,
        "food": 0,
        "knickknacks": 1,
        "string": 1,
        "toy": 1,
    })



def generate_from_relative_probability(option_probability):
    normalized = []
    options = []
    last = 0.0
    for item, prob in option_probability.items():
        if prob <= 0.:
            continue
        last += prob
        options.append(item)
        normalized.append(last)
    return generate_from_normalized(options, normalized)


def generate_from_normalized(options, normalized_probability):
    die = random.uniform(0, normalized_probability[-1])

    option_selected = None
    for option_check, norm_max in zip(options, normalized_probability):
        if die < norm_max:
            option_selected = option_check
            break
    return option_selected


# All the rooms
rooms = ("BA", "DR", "HW", "KI", "LR", "OF",)

def board_v2():
    # Every room has these spaces
    spaces_general = tuple(range(1, 11)) + ("hole", "t")
    # Special spaces
    spaces_special = ("DR-bed", "HW-bed", "HW-crate", "HW-hole-2", "HW-tree", "LR-bed")
    # Put all the spaces together and sort them
    node_labels = tuple("-".join([str(r), str(s)]) for r in rooms for s in spaces_general) + spaces_special
    node_labels = natsort.natsorted(node_labels)

    # Add all the edges. From board v2 (played 5.30.2022)
    board = nx.Graph()
    board.add_nodes_from(node_labels)
    board.add_edges_from([
        ("BA-1", "BA-2"),
        ("BA-2", "BA-3"),
        ("BA-2", "BA-4"),
        ("BA-2", "BA-hole"),
        ("BA-3", "BA-5"),
        ("BA-3", "BA-hole"),
        ("BA-3", "HW-5"),
        ("BA-4", "BA-5"),
        ("BA-4", "BA-6"),
        ("BA-4", "BA-7"),
        ("BA-5", "BA-7"),
        ("BA-5", "BA-t"),
        ("BA-5", "HW-5"),
        ("BA-6", "BA-8"),
        ("BA-7", "BA-9"),
        ("BA-7", "BA-t"),
        ("BA-8", "BA-9"),
        ("BA-9", "BA-10"),
        ("BA-9", "HW-10"),
        # 21:14
        ("DR-1", "DR-2"),
        ("DR-1", "DR-5"),
        ("DR-1", "DR-6"),
        ("DR-1", "HW-crate"),
        ("DR-1", "HW-tree"),
        ("DR-1", "KI-7"),
        ("DR-2", "DR-3"),
        ("DR-2", "DR-8"),
        ("DR-2", "DR-t"),
        ("DR-3", "DR-4"),
        ("DR-3", "DR-bed"),
        ("DR-3", "KI-9"),
        ("DR-4", "DR-7"),
        ("DR-4", "DR-8"),
        ("DR-4", "DR-bed"),
        ("DR-5", "DR-6"),
        ("DR-5", "DR-9"),
        ("DR-5", "HW-crate"),
        ("DR-5", "HW-tree"),
        ("DR-6", "DR-9"),
        ("DR-6", "DR-t"),
        ("DR-7", "DR-8"),
        ("DR-7", "DR-t"),
        ("DR-8", "DR-bed"),
        ("DR-8", "DR-hole"),
        ("DR-9", "DR-10"),
        ("DR-9", "LR-1"),
        ("DR-10", "DR-hole"),
        ("DR-10", "DR-t"),
        ("DR-10", "LR-2"),
        ("DR-bed", "KI-10"),
        ("DR-hole", "LR-2"),
        # 21:20
        ("HW-1", "HW-2"),
        ("HW-1", "HW-3"),
        ("HW-1", "HW-bed"),
        ("HW-1", "HW-hole"),
        ("HW-2", "HW-3"),
        ("HW-2", "HW-bed"),
        ("HW-2", "OF-2"),
        ("HW-3", "HW-hole"),
        ("HW-3", "HW-t"),
        ("HW-3", "KI-1"),
        ("HW-4", "HW-5"),
        ("HW-4", "HW-crate"),
        ("HW-4", "HW-t"),
        ("HW-4", "KI-7"),
        ("HW-4", "OF-8"),
        ("HW-5", "HW-6"),
        ("HW-5", "HW-crate"),
        ("HW-5", "HW-tree"),
        ("HW-5", "BA-3"),
        ("HW-5", "BA-5"),
        ("HW-6", "HW-7"),
        ("HW-6", "HW-tree"),
        ("HW-6", "LR-1"),
        ("HW-7", "HW-8"),
        ("HW-7", "HW-9"),
        ("HW-7", "HW-hole-2"),
        ("HW-8", "LR-3"),
        ("HW-8", "LR-bed"),
        ("HW-8", "HW-hole-2"),
        ("HW-9", "HW-10"),
        ("HW-9", "HW-hole-2"),
        ("HW-10", "BA-9"),
        # 21:25
        ("KI-1", "KI-2"),
        ("KI-1", "KI-4"),
        ("KI-1", "KI-7"),
        ("KI-2", "KI-4"),
        ("KI-2", "KI-5"),
        ("KI-2", "KI-t"),
        ("KI-3", "KI-5"),
        ("KI-3", "KI-6"),
        ("KI-3", "KI-t"),
        ("KI-4", "KI-5"),
        ("KI-4", "KI-7"),
        ("KI-4", "KI-8"),
        ("KI-5", "KI-6"),
        ("KI-5", "KI-8"),
        ("KI-5", "KI-t"),
        ("KI-6", "KI-8"),
        ("KI-6", "KI-10"),
        ("KI-6", "KI-hole"),
        ("KI-8", "KI-9"),
        ("KI-8", "KI-10"),
        ("KI-9", "KI-10"),
        ("KI-10", "KI-hole"),
        #21:28
        ("LR-1", "LR-2"),
        ("LR-1", "LR-3"),
        ("LR-1", "LR-4"),
        ("LR-2", "LR-5"),
        ("LR-2", "LR-6"),
        ("LR-3", "LR-4"),
        ("LR-3", "LR-7"),
        ("LR-3", "LR-8"),
        ("LR-3", "LR-bed"),
        ("LR-4", "LR-5"),
        ("LR-4", "LR-7"),
        ("LR-4", "LR-t"),
        ("LR-5", "LR-6"),
        ("LR-5", "LR-t"),
        ("LR-6", "LR-9"),
        ("LR-6", "LR-t"),
        ("LR-7", "LR-8"),
        ("LR-7", "LR-t"),
        ("LR-8", "LR-9"),
        ("LR-8", "LR-bed"),
        ("LR-8", "LR-hole"),
        ("LR-8", "LR-t"),
        ("LR-9", "LR-10"),
        ("LR-9", "LR-hole"),
        ("LR-9", "LR-t"),
        # 21:33
        ("OF-1", "OF-2"),
        ("OF-1", "OF-4"),
        ("OF-2", "OF-3"),
        ("OF-2", "OF-4"),
        ("OF-2", "OF-5"),
        ("OF-2", "OF-hole"),
        ("OF-3", "OF-5"),
        ("OF-3", "OF-8"),
        ("OF-3", "OF-hole"),
        ("OF-4", "OF-5"),
        ("OF-4", "OF-7"),
        ("OF-5", "OF-6"),
        ("OF-6", "OF-7"),
        ("OF-6", "OF-8"),
        ("OF-6", "OF-10"),
        ("OF-7", "OF-10"),
        ("OF-8", "OF-10"),
        ("OF-9", "OF-10"),
        ("OF-10", "OF-t"),
        #21:36
    ])

    return board





