from dataclasses import dataclass

BOARD_SIZE = 8
NUM_SQUARES = BOARD_SIZE * BOARD_SIZE


@dataclass(frozen=True, slots=True)
class Square:
    index: int

    def __post_init__(self) -> None:
        if not 0 <= self.index < NUM_SQUARES:
            raise ValueError("Square index must be between 0 and 63.")

    @property
    def file(self) -> int:
        return self.index % BOARD_SIZE

    @property
    def rank(self) -> int:
        return self.index // BOARD_SIZE

    @classmethod
    def from_notation(cls, notation: str) -> "Square":
        if len(notation) != 2:
            raise ValueError(f"Invalid square notation: {notation}")

        file = notation[0]
        rank = notation[1]

        if file not in "abcdefgh":
            raise ValueError(f"Invalid file: {file}")

        if rank not in "12345678":
            raise ValueError(f"Invalid rank: {rank}")

        file_index = ord(file) - ord("a")
        rank_index = int(rank) - 1

        return cls(rank_index * BOARD_SIZE + file_index)

    def to_notation(self) -> str:
        file = chr(ord("a") + self.file)
        rank = str(self.rank + 1)

        return f"{file}{rank}"
