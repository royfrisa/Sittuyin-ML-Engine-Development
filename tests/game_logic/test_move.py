from backend.app.domain.sittuyin.move import Move
from backend.app.domain.sittuyin.square import Square


def test_move_stores_source_and_destination():
    from_square = Square.from_notation("e4")
    to_square = Square.from_notation("e5")

    move = Move(
        from_square=from_square,
        to_square=to_square,
    )

    assert move.from_square == from_square
    assert move.to_square == to_square


def test_move_can_be_created_from_notation():
    move = Move(
        from_square=Square.from_notation("e4"),
        to_square=Square.from_notation("e5"),
    )
    assert move.from_square.to_notation() == "e4"
    assert move.to_square.to_notation() == "e5"
