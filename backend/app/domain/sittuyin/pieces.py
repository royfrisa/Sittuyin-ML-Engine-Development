from dataclasses import dataclass
from enum import Enum


class Color(str, Enum):
    RED = "red"
    BLACK = "black"


class PieceType(str, Enum):
    KING = "king"
    GENERAL = "general"
    ELEPHANT = "elephant"
    HORSE = "horse"
    CHARIOT = "chariot"
    PAWN = "pawn"


@dataclass(frozen=True, slots=True)
class Piece:
    color: Color
    piece_type: PieceType
