"""
BerryField class for HW 8 - Bears & Berries
Author: Jimmy Chen
"""

class BerryField:
    # adjacent cells (8-neighbors)
    ADJ = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, grid, bears, tourists):
        self.grid = grid
        self.n = len(grid)
        self.active_bears = bears
        self.active_tourists = tourists

    def in_bounds(self, r, c):
        """Check if the given row and column are within the bounds of the grid."""
        return 0 <= r < self.n and 0 <= c < self.n

    def berry_total(self):
        """Calculate the total number of berries in the grid."""
        return sum(sum(row) for row in self.grid)

    def __str__(self) -> str:
        """Return a string representation of the BerryField."""
        bear_pos = {(b.row, b.col) for b in self.active_bears}
        tourist_pos = {(t.row, t.col) for t in self.active_tourists}

        rows = []
        for r in range(self.n):
            line = []
            for c in range(self.n):
                char = f"{self.grid[r][c]:>4}"
                if (r, c) in bear_pos and (r, c) in tourist_pos:
                    char = f"{'X':>4}"
                elif (r, c) in bear_pos:
                    char = f"{'B':>4}"
                elif (r, c) in tourist_pos:
                    char = f"{'T':>4}"
                line.append(char)
            rows.append("".join(line).rstrip())
        return "\n".join(rows)

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
