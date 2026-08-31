import random

class MapGenerator:
    def __init__(self, width=60, height=18):
        self.width = width
        self.height = height

    def generate_level(self, player_level):
        """Generates a procedural map with walls, floor, doors, terminals, vendors, and enemies."""
        # Fill map with walls (#)
        grid = [["#" for _ in range(self.width)] for _ in range(self.height)]
        
        # Room placement
        rooms = []
        num_rooms = random.randint(4, 7)
        for _ in range(num_rooms):
            rw = random.randint(6, 12)
            rh = random.randint(4, 8)
            rx = random.randint(1, self.width - rw - 1)
            ry = random.randint(1, self.height - rh - 1)
            
            # Check overlap
            overlap = False
            for (ox, oy, ow, oh) in rooms:
                if (rx < ox + ow and rx + rw > ox and
                    ry < oy + oh and ry + rh > oy):
                    overlap = True
                    break
            
            if not overlap:
                rooms.append((rx, ry, rw, rh))
                # Carve room
                for y in range(ry, ry + rh):
                    for x in range(rx, rx + rw):
                        grid[y][x] = "."

        # Connect rooms with corridors
        for i in range(len(rooms) - 1):
            x1, y1, w1, h1 = rooms[i]
            x2, y2, w2, h2 = rooms[i+1]
            
            cx1, cy1 = x1 + w1 // 2, y1 + h1 // 2
            cx2, cy2 = x2 + w2 // 2, y2 + h2 // 2
            
            # Draw horizontal/vertical corridors
            if random.random() < 0.5:
                # Horiz first
                for x in range(min(cx1, cx2), max(cx1, cx2) + 1):
                    grid[cy1][x] = "."
                for y in range(min(cy1, cy2), max(cy1, cy2) + 1):
                    grid[y][cx2] = "."
            else:
                # Vert first
                for y in range(min(cy1, cy2), max(cy1, cy2) + 1):
                    grid[y][cx1] = "."
                for x in range(min(cx1, cx2), max(cx1, cx2) + 1):
                    grid[cy2][x] = "."

        # Find empty spots for Player, Exit, Enemies, Terminals, Vendors
        empty_spots = []
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if grid[y][x] == ".":
                    empty_spots.append((x, y))
                    
        random.shuffle(empty_spots)
        
        # Player spawn
        p_x, p_y = empty_spots.pop()
        
        # Exit Elevator spawn
        e_x, e_y = empty_spots.pop()
        grid[e_y][e_x] = "E"
        
        # Vendor spawn
        v_x, v_y = empty_spots.pop()
        grid[v_y][v_x] = "V"
        
        # Spawn terminals (T)
        num_terminals = random.randint(2, 4)
        terminal_positions = []
        for _ in range(num_terminals):
            if empty_spots:
                tx, ty = empty_spots.pop()
                grid[ty][tx] = "T"
                terminal_positions.append((tx, ty))

        # Spawn enemies
        num_enemies = random.randint(3, 5)
        enemies = []
        for i in range(num_enemies):
            if empty_spots:
                ex, ey = empty_spots.pop()
                grid[ey][ex] = "M" # Mob
                
                # Determine enemy type and level
                lvl = max(1, player_level + random.randint(-1, 2))
                hp = 40 + lvl * 15
                dmg = 8 + lvl * 3
                xp = 20 + lvl * 10
                credits_reward = 30 + lvl * 15
                
                enemies.append({
                    "name": f"Corpo Patrol v{lvl}",
                    "hp": hp,
                    "max_hp": hp,
                    "level": lvl,
                    "damage": dmg,
                    "xp_reward": xp,
                    "credits_reward": credits_reward,
                    "x": ex,
                    "y": ey
                })

        return {
            "grid": grid,
            "player_start": (p_x, p_y),
            "exit": (e_x, e_y),
            "vendor": (v_x, v_y),
            "enemies": enemies,
            "terminals": terminal_positions
        }
