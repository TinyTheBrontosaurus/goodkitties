from goodkitties.engine import state


def test_turn_order():

    # Arrange
    out = state.TurnController()

    # Act
    actual = [(x.stage, x.kitty_stage, x.actions_left) for x in out]

    # Assert
    actuali = 0
    assert actual[actuali][0] == "supply"
    actuali += 1
    assert actual[actuali][0] == "mice"
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 4
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 3
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 2
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 1
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 4
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 3
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 2
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 1
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 4
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 3
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 2
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 1
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 4
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 3
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 2
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 1
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 4
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 3
    actuali += 1
    assert actual[actuali][0] == "kitties"
    assert actual[actuali][1] == "actions"
    assert actual[actuali][2] == 2
    actuali += 1
    assert actual[actuali][0] == "dog"
    actuali += 1

    assert actuali == len(actual)
