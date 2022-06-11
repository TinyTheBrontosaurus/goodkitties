from goodkitties.engine import state


def test_turn_order():

    # Arrange
    out = state.TurnController()

    # Act
    actual = [(x.stage, x.kitty_stage, x.actions_left) for x in out]

    # Assert
    print(actual)
