import pytest

from backend.app.domain.sittuyin.board import NUM_SQUARES, Board
from backend.app.domain.sittuyin.pieces import Color, Piece, PieceType
from backend.app.domain.sittuyin.square import Square


def test_empty_board_has_64_squares():
    board = Board.empty()

    assert len(board.squares) == NUM_SQUARES
    assert all(square is None for square in board.squares)


def test_board_can_place_and_retrieve_piece():
    board = Board.empty()

    king = Piece(
        color=Color.RED,
        piece_type=PieceType.KING,
    )

    square = Square.from_notation("e4")

    board.set_piece(square, king)

    assert board.get_piece(square) == king


def test_board_can_remove_piece():
    board = Board.empty()

    king = Piece(
        color=Color.RED,
        piece_type=PieceType.KING,
    )

    square = Square.from_notation("e4")

    board.set_piece(square, king)
    board.set_piece(square, None)

    assert board.get_piece(square) is None


def test_board_requires_64_squares():
    with pytest.raises(ValueError):
        Board([None] * 63)
