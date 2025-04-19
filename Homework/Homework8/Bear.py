"""
This is a class for a bear. It is a part of hw 8 bears and berries.

Author: Jimmy Chen
Version: 1
"""
class Bear:
    def __init__(self, row: int, col: int, direction: str):
        self.row = row
        self.col = col
        self.dir = direction
        self.asleep_turns = 0       # not used yet, but handy for Part 2/3

    def __str__(self) -> str:
        return f"Bear at ({self.row},{self.col}) moving {self.dir}"


