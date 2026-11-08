from dataclasses import dataclass

from .pieces import Piece
from .square import Square

BOARD_SIZE = 8
NUM_SQUARES = BOARD_SIZE * BOARD_SIZE


@dataclass
class Board:
    squares: list[Piece | None]

    def __post_init__(self) -> None:
        if len(self.squares) != NUM_SQUARES:
            raise ValueError(f"Board must contain exactly {NUM_SQUARES} squares.")

    @classmethod
    def empty(cls) -> "Board":
        return cls([None] * NUM_SQUARES)

    def get_piece(self, square: Square) -> Piece | None:
        return self.squares[square.index]

    def set_piece(self, square: Square, piece: Piece | None) -> None:
        self.squares[square.index] = piece
