import random
from snappiershot import Snapshot
from goodkitties.engine.basic import generate_item

def test_generate_item(snapshot: Snapshot):

    # Arrange
    random.seed(17)
    answers = {}
    count = 10000

    # Act
    for _ in range(count):
        item = generate_item()
        answers[item] = answers.get(item, 0) + 1

    # Assert
    assert count == sum((x for x in answers.values()))
    snapshot.assert_match(answers)
