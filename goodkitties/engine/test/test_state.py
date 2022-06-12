from goodkitties.engine import state


def test_nested_phase():

    # Arrange
    out = state.NestedPhase({"one": None, "two": None, "three": None})

    # Act
    actual = [x for x in out]

    # Assert
    assert actual == [["one"], ["two"], ["three"]]


def test_nested_phase_2():

    # Arrange
    out = state.NestedPhase({"one": None,
                             "two": state.NestedPhase({"A": None, "B":  None}),
                             "three": None})

    # Act
    actual = [x for x in out]

    # Assert
    assert actual == [["one"], ["two", "A"], ["two", "B"], ["three"]]


def test_repeater():
    # Arrange
    out = state.Repeater(3, state.NestedPhase({"A": None, "B": None}))

    # Act
    actual = [x for x in out]

    # Assert
    assert actual == [["A"], ["B"], ["A"], ["B"], ["A"], ["B"]]

def test_default_turn_phase():
    # Arrange
    out = state.default_turn_phase()

    # Act
    actual = [x for x in out]

    # Assert
    assert actual == [["one"], ["two", "A"], ["two", "B"], ["three"]]


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
