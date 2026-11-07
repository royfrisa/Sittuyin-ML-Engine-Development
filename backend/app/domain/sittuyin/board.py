from dataclasses import dataclass

from .pieces import Piece

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

    def get_piece(self, square: int) -> Piece | None:
        return self.squares[square]

    def set_piece(self, square: int, piece: Piece | None) -> None:
        self.squares[square] = piece
