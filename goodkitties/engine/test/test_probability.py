import random
from snappiershot import Snapshot
from goodkitties.engine import probability

def test_generate_item(snapshot: Snapshot):

    # Arrange
    random.seed(17)
    answers = {}
    count = 10000
    probs = {
        "electronics": 1,
        "food": 0,
        "knickknacks": 1,
        "string": 1,
        "toy": 1,
    }

    # Act
    for _ in range(count):
        item = probability.generate_from_relative_probability(probs)
        answers[item] = answers.get(item, 0) + 1

    # Assert
    assert count == sum((x for x in answers.values()))
    snapshot.assert_match(answers)
