import pytest

from backend.app.domain.sittuyin.square import Square


def test_first_square_is_a1():
    square = Square.from_notation("a1")
    assert square.index == 0
    assert square.to_notation() == "a1"


def test_middle_square_is_e4():
    square = Square.from_notation("e4")
    assert square.index == 28
    assert square.to_notation() == "e4"


def test_last_square_is_h8():
    square = Square.from_notation("h8")
    assert square.index == 63
    assert square.to_notation() == "h8"


def test_square_file_and_rank():
    square = Square.from_notation("e4")
    assert square.file == 4
    assert square.rank == 3


def test_invalid_square_index():
    with pytest.raises(ValueError):
        Square(64)


def test_invalid_notation():
    with pytest.raises(ValueError):
        Square.from_notation("z9")
