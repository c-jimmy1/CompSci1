"""
BerryField class for HW 8 – Bears & Berries
Author: Jimmy Chen
"""

class BerryField:
    # adjacent cells (8-neighbors)
    ADJ = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, grid, bears=None, tourists=None):
        self.grid = grid
        self.n = len(grid)
        self.active_bears = bears or []
        self.active_tourists = tourists or []

    def in_bounds(self, r, c):
        """Check if the given row and column are within the bounds of the grid."""
        return 0 <= r < self.n and 0 <= c < self.n

    def berry_total(self):
        """Calculate the total number of berries in the grid."""
        return sum(sum(row) for row in self.grid)

    def __str__(self):
        """Return a string representation of the BerryField."""
        bear_pos = {(b.row, b.col) for b in self.active_bears}
        tourist_pos = {(t.row, t.col) for t in self.active_tourists}

        lines = []
        for r in range(self.n):
            row = []
            for c in range(self.n):
                if (r, c) in bear_pos and (r, c) in tourist_pos:
                    cell = "X"
                elif (r, c) in bear_pos:
                    cell = "B"
                elif (r, c) in tourist_pos:
                    cell = "T"
                else:
                    cell = str(self.grid[r][c])
                row.append(f"{cell:>4}")
            lines.append("".join(row))
        return "\n".join(lines)

    def grow(self):
        """Grow the berries in the field according to the rules:
        1) every cell holding 1-9 berries gets +1
        2) any zero-cell adjacent (in 8-neighbourhood) to a 10 becomes 1"""
        
        # every cell holding 1‑9 berries gets +1
        for r in range(self.n):
            for c in range(self.n):
                if 1 <= self.grid[r][c] < 10:
                    self.grid[r][c] += 1

        # any zero‑cell adjacent (in 8‑neighbourhood) to a 10 becomes 1
        to_seed = []
        for r in range(self.n):
            for c in range(self.n):
                if self.grid[r][c] == 0:
                    for dr, dc in BerryField.ADJ:
                        nr, nc = r + dr, c + dc
                        if self.in_bounds(nr, nc) and self.grid[nr][nc] == 10:
                            to_seed.append((r, c))
                            break
        for r, c in to_seed:
            self.grid[r][c] = 1
