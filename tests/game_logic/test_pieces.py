from backend.app.domain.sittuyin.pieces import (
    Color,
    Piece,
    PieceType,
)


def test_create_red_king():
    king = Piece(
        color=Color.RED,
        piece_type=PieceType.KING,
    )

    assert king.color == Color.RED
    assert king.piece_type == PieceType.KING


def test_piece_colors_are_distinct():
    assert Color.RED != Color.BLACK


def test_sittuyin_has_six_piece_types():
    assert len(PieceType) == 6
