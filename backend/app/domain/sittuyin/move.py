from dataclasses import dataclass

from .square import Square


@dataclass(frozen=True, slots=True)
class Move:
    from_square: Square
    to_square: Square
