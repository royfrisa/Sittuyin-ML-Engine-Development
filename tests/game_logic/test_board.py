import pytest
from backend.app.domain.sittuyin.board import NUM_SQUARES, Board
from backend.app.domain.sittuyin.pieces import Color, Piece, PieceType

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

    board.set_piece(0, king)

    assert board.get_piece(0) == king


def test_board_can_remove_piece():
    board = Board.empty()

    king = Piece(
        color=Color.RED,
        piece_type=PieceType.KING,
    )

    board.set_piece(0, king)
    board.set_piece(0, None)

    assert board.get_piece(0) is None

def test_board_requires_64_squares():
    with pytest.raises(ValueError):
        Board([None] * 63)
