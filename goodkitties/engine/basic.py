import networkx as nx

import matplotlib.pyplot as plt


def main(_argv):

    office = nx.Graph()

    office.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "T", "mousehole"])
    # Note: For ease, order all the edges in numerical order. With low #'d node always going first
    office.add_edges_from([
        (1, 2),
        (1, 4),
        (2, 3),
        (2, 5),
        (2, "mousehole"),
        (3, 5),
        (3, 8),
        (3, "mousehole"),
        (4, 5),
        (4, 7),
        (5, 6),
        (6, 7),
        (6, 8),
        (6, 10),
        (7, 10),
        (8, 10),
        (9, 10),
        (10, "T"),
        ])
    subax1 = plt.subplot(1, 1, 1)
    nx.draw(office, with_labels=True, font_weight='bold')
    plt.show()


def demo():
    """
    https://networkx.org/documentation/stable/tutorial.html
    :return:
    """
    G = nx.petersen_graph()
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    subax2 = plt.subplot(122)
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    plt.show()
