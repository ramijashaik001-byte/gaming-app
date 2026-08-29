from engine.renderer import BOLD, RED, RESET, GREEN, CYAN, YELLOW, PINK, GRAY

class World:
    def __init__(self, level_data):
        self.grid = level_data["grid"]
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.exit_pos = level_data["exit"]
        self.vendor_pos = level_data["vendor"]
        self.enemies = level_data["enemies"]
        self.terminals = level_data["terminals"]

    def is_walkable(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            # Wall blocks movement
            return self.grid[y][x] != "#"
        return False

    def get_enemy_at(self, x, y):
        for enemy in self.enemies:
            if enemy["x"] == x and enemy["y"] == y and enemy["hp"] > 0:
                return enemy
        return None

    def trigger_interaction(self, x, y, player):
        """Returns action type and data if player interacts with a special tile."""
        tile = self.grid[y][x]
        
        # Check enemy
        enemy = self.get_enemy_at(x, y)
        if enemy:
            return "combat", enemy

        if tile == "T":
            # Check if terminal already hacked
            if (x, y) in self.terminals:
                return "hack", (x, y)
        elif tile == "V":
            return "vendor", (x, y)
        elif tile == "E":
            return "exit", (x, y)
            
        return None, None

    def remove_terminal(self, x, y):
        if (x, y) in self.terminals:
            self.terminals.remove((x, y))
        self.grid[y][x] = "." # Clear terminal tile

    def remove_enemy(self, enemy):
        # Find and mark cell as empty floor
        for e in self.enemies:
            if e["x"] == enemy["x"] and e["y"] == enemy["y"]:
                e["hp"] = 0
                self.grid[enemy["y"]][enemy["x"]] = "."

    def render_map(self, player_x, player_y):
        """Returns the map lines ready to be rendered in the renderer's main box."""
        map_lines = []
        for y in range(self.height):
            row_str = ""
            for x in range(self.width):
                if x == player_x and y == player_y:
                    row_str += BOLD + PINK + "@" + RESET # Player
                else:
                    char = self.grid[y][x]
                    if char == "#":
                        row_str += GRAY + "█" + RESET # Wall
                    elif char == ".":
                        row_str += DIM + GRAY + "·" + RESET # Floor
                    elif char == "T":
                        row_str += CYAN + "T" + RESET # Hacking terminal
                    elif char == "V":
                        row_str += YELLOW + "V" + RESET # Vendor
                    elif char == "E":
                        row_str += GREEN + "E" + RESET # Exit elevator
                    elif char == "M":
                        # Check if enemy is still alive
                        enemy = self.get_enemy_at(x, y)
                        if enemy and enemy["hp"] > 0:
                            row_str += RED + "M" + RESET # Mob
                        else:
                            row_str += DIM + GRAY + "·" + RESET
                    else:
                        row_str += char
            map_lines.append(row_str)
        return map_lines
