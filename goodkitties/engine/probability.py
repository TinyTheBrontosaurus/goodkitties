"""
Package with "generic" probability methods. Not specific to any game. Things like replacement and dice rolls.
"""
import math
import random


def roll_d(sides: int):
    """Roll an n-sided die. Returns in integer in [1, sides] in uniform distribution"""
    val = random.uniform(sides)
    return int(math.floor(val)) + 1


def roll_d4():
    """Roll a 4-side die. Return integer in [1, 4]"""
    return roll_d(4)


def roll_d6():
    """Roll a 6-side die. Return integer in [1, 6]"""
    return roll_d(6)


def roll_d8():
    """Roll a 8-side die. Return integer in [1, 8]"""
    return roll_d(8)


def roll_d10():
    """Roll a 10-side die. Return integer in [1, 10]"""
    return roll_d(10)


def roll_d12():
    """Roll a 12-side die. Return integer in [1, 12]"""
    return roll_d(12)


def roll_d20():
    """Roll a 20-side die. Return integer in [1, 20]"""
    return roll_d(20)


def roll_d100():
    """Roll a 100-side die. Return integer in [1, 100]"""
    return roll_d(100)


def generate_from_relative_probability(element_probability: dict):
    """
    Return a random element based upon set probability.

    :param element_probability: Input a dictionary with keys as elements and values as relative probabilities. Values of
    0 are fully ignored.
        Sample inputs:
        element_probability -> {'a': 1, 'b': 7, 'c': 22}
        a has 1/30 chance. b has 7/30 chance. c has 22/30 chance.
    :return: Randomly selected element
    """
    normalized = []
    elements = []
    last = 0.0
    for item, prob in element_probability.items():
        if prob <= 0.:
            continue
        last += prob
        elements.append(item)
        normalized.append(last)
    return _generate_from_normalized(elements, normalized)


def _generate_from_normalized(elements, normalized_probability):
    """
    Return a random element based upon set probability.
    Input is normalized such that a uniform distribution result can be mapped to an element.
    Sample inputs:
       elements -> ['a', 'b', 'c']
       normalized_probability -> [1, 8, 30]
       c has 22/30 chance. b has 7/30 chance. a has 1/30 chance

    :param elements: Parallel array. list of elements, one of which is returned
    :param normalized_probability: Parallel array. If the number drawn is between the previous index and this index,
    return the element at this index. Values are expected to be floats sorted in increasing order with the first value
    greater than 0.
    :return: Element at that randomly selected index
    """

    # Handle edge case in case it's not initialized somehow
    element_selected = elements[0]

    # Draw random number and find the element
    rand_val = random.uniform(0, normalized_probability[-1])
    for element_check, norm_max in zip(elements, normalized_probability):
        if rand_val < norm_max:
            element_selected = element_check
            break
    return element_selected
