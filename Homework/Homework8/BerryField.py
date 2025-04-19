"""
This is a class for a berry field. It's a class for hw 8. This class
manages the berry field and the berries in it.
Author: Jimmy Chen
Version: 1
"""


class BerryField:
    def __init__(self, grid, bears=None, tourists=None):
        self.grid = grid
        self.n = len(grid)
        self.active_bears = bears or []
        self.active_tourists = tourists or []

    def __str__(self) -> str:
        bear_pos = {(b.row, b.col): b for b in self.active_bears}
        tourist_pos = {(t.row, t.col): t for t in self.active_tourists}

        rows = []
        for r in range(self.n):
            line = []
            for c in range(self.n):
                char = f"{self.grid[r][c]:>4}"          # default = berries
                if (r, c) in bear_pos and (r, c) in tourist_pos:
                    char = f"{'X':>4}"
                elif (r, c) in bear_pos:
                    char = f"{'B':>4}"
                elif (r, c) in tourist_pos:
                    char = f"{'T':>4}"
                line.append(char)
            rows.append("".join(line))
        return "\n".join(rows)
    
    def berry_total(self) -> int:
        """Return the total number of berries currently in the field."""
        return sum(sum(row) for row in self.grid)
    
    