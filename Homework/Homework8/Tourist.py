"""
Tourist class for HW 8 - Bears & Berries
Author: Jimmy Chen
"""

class Tourist:
    """Tourist that watches bears (or gets bored / scared)."""

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.turns_without_bear = 0

    def __str__(self):
        return (f"Tourist at ({self.row},{self.col}), "
                f"{self.turns_without_bear} turns without seeing a bear.")

    def take_turn(self, bears):
        """Update counters and return True if the tourist leaves."""
        seen = 0
        for b in bears:
            # Manhattan distance ≤ 4
            if abs(b.row - self.row) + abs(b.col - self.col) <= 4:
                seen += 1

        if seen:
            self.turns_without_bear = 0
        else:
            self.turns_without_bear += 1

        return (seen >= 3) or (self.turns_without_bear >= 3)
