"""
This is a class for tourist objects. This holds information for a tourist in the bears
and berries simulation.

Author: Jimmy Chen
Version: 1
"""

class Tourist:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.turns_without_bear = 0

    def __str__(self) -> str:
        return (f"Tourist at ({self.row},{self.col}), "
                f"{self.turns_without_bear} turns without seeing a bear.")
        
    