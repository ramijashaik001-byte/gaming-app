import random
from engine.renderer import BOLD, RED, RESET, GREEN, CYAN, YELLOW, PINK, GRAY

class HackingGame:
    def __init__(self, player, difficulty=1):
        self.player = player
        self.difficulty = difficulty
        self.grid_size = 5
        self.hex_pool = ["1C", "E9", "7A", "BD", "55", "FF"]
        self.grid = []
        self.target_sequence = []
        self.max_buffer = 4
        self.buffer = []
        
        # Cursor coordinates
        self.cursor_x = 0
        self.cursor_y = 0
        self.select_vertical = False # Start selecting in row (horizontal)
        
        self.completed = False
        self.failed = False
        self.generate_puzzle()

    def generate_puzzle(self):
        # Create a 5x5 grid of random hex codes
        self.grid = [[random.choice(self.hex_pool) for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        # Generate a valid solution of size 2-3 depending on difficulty
        seq_length = 2 + (self.difficulty > 2)
        curr_x, curr_y = 0, 0
        horizontal = True
        
        temp_seq = []
        visited = set()
        
        for _ in range(seq_length * 2):
            if horizontal:
                next_x = random.randint(0, self.grid_size - 1)
                while (next_x, curr_y) in visited:
                    next_x = random.randint(0, self.grid_size - 1)
                curr_x = next_x
            else:
                next_y = random.randint(0, self.grid_size - 1)
                while (curr_x, next_y) in visited:
                    next_y = random.randint(0, self.grid_size - 1)
                curr_y = next_y
            
            visited.add((curr_x, curr_y))
            temp_seq.append(self.grid[curr_y][curr_x])
            horizontal = not horizontal

        # Slice to construct the sequence
        start = random.randint(0, len(temp_seq) - seq_length)
        self.target_sequence = temp_seq[start:start + seq_length]

    def draw_grid_strings(self):
        lines = []
        lines.append(f"{BOLD}{PINK}BREACH PROTOCOL v3.2{RESET}")
        lines.append(f"Target Sequence: {CYAN}{' - '.join(self.target_sequence)}{RESET}")
        lines.append(f"Buffer: {YELLOW}[{', '.join(self.buffer)}]{RESET} ({len(self.buffer)}/{self.max_buffer})")
        lines.append("")

        # Column indices
        header = "   " + "  ".join(f"C{i}" for i in range(self.grid_size))
        lines.append(GRAY + header + RESET)

        for r in range(self.grid_size):
            row_str = f"R{r} "
            for c in range(self.grid_size):
                cell = self.grid[r][c]
                # Highlight if cursor is on it
                if r == self.cursor_y and c == self.cursor_x:
                    cell_str = f"{BOLD}{YELLOW}[{cell}]{RESET}"
                elif (self.select_vertical and c == self.cursor_x) or (not self.select_vertical and r == self.cursor_y):
                    cell_str = f"{CYAN} {cell} {RESET}"
                else:
                    cell_str = f" {cell} "
                row_str += cell_str
            lines.append(row_str)
            
        lines.append("")
        if self.select_vertical:
            lines.append(f"{CYAN}Direction: VERTICAL. Select a cell in column {self.cursor_x}.{RESET}")
        else:
            lines.append(f"{CYAN}Direction: HORIZONTAL. Select a cell in row {self.cursor_y}.{RESET}")
            
        lines.append("Use [WASD] to move, [Enter] to submit code.")
        return lines

    def move_cursor(self, direction):
        if self.select_vertical:
            # Move only vertically in the column
            if direction == "w":
                self.cursor_y = (self.cursor_y - 1) % self.grid_size
            elif direction == "s":
                self.cursor_y = (self.cursor_y + 1) % self.grid_size
        else:
            # Move only horizontally in the row
            if direction == "a":
                self.cursor_x = (self.cursor_x - 1) % self.grid_size
            elif direction == "d":
                self.cursor_x = (self.cursor_x + 1) % self.grid_size

    def select_cell(self):
        code = self.grid[self.cursor_y][self.cursor_x]
        if code == "--":
            return # Already used

        self.buffer.append(code)
        self.grid[self.cursor_y][self.cursor_x] = "--"
        
        # Check success
        # If the target sequence is a substring of the buffer
        buffer_str = "".join(self.buffer)
        target_str = "".join(self.target_sequence)
        
        if target_str in buffer_str:
            self.completed = True
            reward = self.difficulty * 150
            self.player.credits += reward
            return f"{BOLD}{GREEN}ACCESS GRANTED!{RESET} Hacked terminal and extracted {YELLOW}₵{reward}{RESET}."

        if len(self.buffer) >= self.max_buffer:
            self.failed = True
            return f"{BOLD}{RED}BREACH LOCKOUT!{RESET} Intrustion detection system activated."

        # Alternate select direction
        self.select_vertical = not self.select_vertical
        return None
