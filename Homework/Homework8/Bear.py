"""
Bear class for HW 8 - Bears & Berries
Author: Jimmy Chen
"""

class Bear:
    """Bear that walks, eats, and sleeps."""

    DIR_VECS = {
        "N":  (-1, 0),  "S":  (1, 0),
        "E":  (0, 1),   "W":  (0, -1),
        "NE": (-1, 1),  "NW": (-1, -1),
        "SE": (1, 1),   "SW": (1, -1)
    }

    def __init__(self, row: int, col: int, direction: str):
        self.row = row
        self.col = col
        self.dir = direction
        self.asleep_turns = 0

    def _tourist_here(self, tourists):
        """Private method to check if a tourist is at the bear's location."""
        for t in tourists:
            if t.row == self.row and t.col == self.col:
                return t
        return None

    def __str__(self):
        """String representation of the bear."""
        s = f"Bear at ({self.row},{self.col}) moving {self.dir}"
        if self.asleep_turns:
            s += f" - Asleep for {self.asleep_turns} more turns"
        return s

    def take_turn(self, field, tourists):
        """Take a turn for the bear, moving and eating berries."""
        messages = []

        # if the bear is asleep, decrement the sleep counter
        if self.asleep_turns:
            self.asleep_turns -= 1
            return messages, False

        # While the bear has not eaten 30 berries
        eaten = 0
        while eaten < 30:
            
            # Check if there is a tourist at the bear's location
            victim = self._tourist_here(tourists)
            if victim:
                messages.append(f"{victim} - Left the Field")
                tourists.remove(victim)
                self.asleep_turns = 2
                break

            # 1) check if the bear is at a berry cell
            cell_berries = field.grid[self.row][self.col]
            need = 30 - eaten
            if cell_berries > need:
                # eat only what is needed and leave the rest
                field.grid[self.row][self.col] = cell_berries - need
                eaten = 30
                break
            else:
                eaten += cell_berries
                field.grid[self.row][self.col] = 0
                if eaten == 30:
                    break

            dr, dc = Bear.DIR_VECS[self.dir]
            nr, nc = self.row + dr, self.col + dc
            if not field.in_bounds(nr, nc):
                messages.append(
                    f"Bear at ({nr},{nc}) moving {self.dir} - Left the Field"
                )
                return messages, True
            self.row, self.col = nr, nc

        return messages, False
