from goodkitties.engine import state


def test_turn_order():

    # Arrange
    out = state.TurnOrder()

    # Act
    actual = [(x. for x in out]