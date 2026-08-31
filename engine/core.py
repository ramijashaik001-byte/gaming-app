import sys
import time
import random
from engine.renderer import Renderer, BOLD, RED, RESET, GREEN, CYAN, YELLOW, PINK, GRAY, ORANGE
from engine.entities import Player, Enemy, Vendor
from engine.world import World
from engine.generator import MapGenerator
from engine.combat import Combat
from engine.hacking import HackingGame

# Fallback dynamic imports to avoid failure during generator build phase
try:
    from data.items import WEAPONS_DATABASE, ARMOR_DATABASE, CONSUMABLES_DATABASE
    from data.world_data import LORE_DATABASE
except ImportError:
    WEAPONS_DATABASE = [{"name": "Mono-Wire", "type": "weapon", "damage": 12, "cost": 0, "description": "Standard neural filament wire."}]
    ARMOR_DATABASE = [{"name": "Polycarbonate Jacket", "type": "armor", "defense": 2, "cost": 0, "description": "Basic street protective gear."}]
    CONSUMABLES_DATABASE = [{"name": "MaxDoc Injector", "type": "consumable", "heal": 50, "cost": 50, "description": "Quick-inject nano-healer."}]
    LORE_DATABASE = ["Corporate systems report no security breaches."]

# Windows keyboard input import
try:
    import msvcrt
    WINDOWS_INPUT = True
except ImportError:
    WINDOWS_INPUT = False

class GameEngine:
    def __init__(self):
        Renderer.init_terminal()
        self.player = None
        self.world = None
        self.generator = MapGenerator()
        self.state = "MAIN_MENU"
        self.running = True
        self.current_combat = None
        self.current_hacking = None
        self.active_vendor = None
        self.vendor_inventory = []
        self.explore_logs = ["Welcome to NeonRogue v1.0. Locate the elevator (E) to descend deeper."]
        self.level_depth = 1

    def read_char(self):
        """Reads a single key input, blocking, cross-platform with arrow fallbacks."""
        if WINDOWS_INPUT:
            ch = msvcrt.getch()
            # Special/Arrow keys (two-byte sequence starting with 0x00 or 0xE0)
            if ch in (b'\x00', b'\xe0'):
                ch2 = msvcrt.getch()
                if ch2 == b'H': return "w" # Up
                if ch2 == b'P': return "s" # Down
                if ch2 == b'K': return "a" # Left
                if ch2 == b'M': return "d" # Right
            try:
                return ch.decode('utf-8').lower()
            except:
                return ""
        else:
            # Fallback for non-Windows (or tests)
            import select
            rlist, _, _ = select.select([sys.stdin], [], [], 10.0)
            if rlist:
                char = sys.stdin.read(1)
                return char.lower()
            return ""

    def add_log(self, text):
        self.explore_logs.append(text)
        if len(self.explore_logs) > 18:
            self.explore_logs.pop(0)

    def start_new_game(self, player_name):
        self.player = Player(player_name)
        self.level_depth = 1
        self.load_level()
        self.state = "EXPLORE"

    def load_level(self):
        self.add_log(f"GENERATING LEVEL {self.level_depth} GRID...")
        level_data = self.generator.generate_level(self.player.level)
        self.world = World(level_data)
        px, py = level_data["player_start"]
        self.player.x = px
        self.player.y = py
        
        # Populate vendor items
        self.vendor_inventory = []
        # Add random items from databases
        for _ in range(3):
            self.vendor_inventory.append(random.choice(WEAPONS_DATABASE))
            self.vendor_inventory.append(random.choice(ARMOR_DATABASE))
            self.vendor_inventory.append(random.choice(CONSUMABLES_DATABASE))
        
        self.add_log(f"Arrived at Sector {self.level_depth}. Ambient system temperature: 24°C.")

    def run(self):
        while self.running:
            if self.state == "MAIN_MENU":
                self.draw_main_menu()
            elif self.state == "EXPLORE":
                self.draw_explore()
            elif self.state == "COMBAT":
                self.draw_combat()
            elif self.state == "HACKING":
                self.draw_hacking()
            elif self.state == "VENDOR":
                self.draw_vendor()
            elif self.state == "INVENTORY":
                self.draw_inventory()
            elif self.state == "STATS":
                self.draw_stats()
            elif self.state == "GAMEOVER":
                self.draw_gameover()
                
            key = self.read_char()
            if key:
                self.handle_input(key)

    def draw_main_menu(self):
        title = " NEON ROGUE v1.0 "
        lines = [
            "",
            f"   {BOLD}{CYAN}███╗   ██╗███████╗ ██████╗ ███╗   ██╗██████╗  ██████╗  ██████╗ ██╗   ██╗███████╗{RESET}",
            f"   {BOLD}{CYAN}████╗  ██║██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔═══██╗██╔════╝ ██║   ██║██╔════╝{RESET}",
            f"   {BOLD}{CYAN}██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║██████╔╝██║   ██║██║  ███╗██║   ██║█████╗  {RESET}",
            f"   {BOLD}{CYAN}██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║██╔══██╗██║   ██║██║   ██║██║   ██║██╔══╝  {RESET}",
            f"   {BOLD}{CYAN}██║ ╚████║███████╗╚██████╔╝██║ ╚████║██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗{RESET}",
            f"   {RESET}{DIM}{GRAY}╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝{RESET}",
            "",
            "                     - A Cyberpunk Console Text RPG -",
            "",
            "                           [N] Start New Game",
            "                           [Q] Quit Simulator",
            "",
            "",
            f"{BOLD}{PINK}Created with Advanced Terminal UI & Dynamic Web Audio Architecture simulation.{RESET}",
            "",
            "Controls Guide:",
            "  Use WASD or Arrow Keys in maps. Press H near terminals, V near Vendors.",
            "  Standard keystroke inputs process choices dynamically."
        ]
        Renderer.draw_screen(title, lines)

    def draw_explore(self):
        hud = Renderer.draw_hud(self.player)
        map_lines = self.world.render_map(self.player.x, self.player.y)
        
        # Side logs
        logs = ["--- SYSTEM ACTIVITY LOG ---"]
        for log in self.explore_logs:
            logs.append(log)
            
        Renderer.draw_screen(f" SECTOR GRID: LEVEL {self.level_depth} ", map_lines, hud_lines=hud, side_box_title=" DATA FEED ", side_box_lines=logs)

    def draw_combat(self):
        hud = Renderer.draw_hud(self.player)
        combat = self.current_combat
        
        # Display enemy details in main panel
        main_lines = [
            f"{BOLD}{RED}HOSTILE TARGET: {combat.enemy.name} (Lvl {combat.enemy.level}){RESET}",
            Renderer.make_progress_bar(combat.enemy.hp, combat.enemy.max_hp, 25, filled_color=RED),
            f"HP: {combat.enemy.hp} / {combat.enemy.max_hp}",
            "",
            "TACTICAL OPTIONS:",
            "  [1] Attack with equipped weapon",
            "  [2] Run Netrunner hacking program",
            "  [3] Inject nano-potion (Consumable)",
            "  [4] Tactical Flee (Escape combat)",
            "",
            "--- COMBAT FEEDS ---"
        ]
        for log in combat.combat_log:
            main_lines.append(log)

        # Draw programs on side panel
        side_lines = ["--- NEURAL PROGRAMS ---"]
        for idx, prog in enumerate(self.player.programs):
            side_lines.append(f"[{idx}] {CYAN}{prog['name']}{RESET} (RAM: {prog['ram_cost']}) - Dmg: {prog['damage']}")

        Renderer.draw_screen(" MELEE ENGAGEMENT HUD ", main_lines, hud_lines=hud, side_box_title=" HACK SLOTS ", side_box_lines=side_lines)

    def draw_hacking(self):
        hud = Renderer.draw_hud(self.player)
        main_lines = self.current_hacking.draw_grid_strings()
        
        # Show lore log preview on side panel
        side_lines = [
            "--- ENCRYPTION DETECT ---",
            "Successfully hacking the node",
            "gives access to direct banking credits",
            "and decodes secret archives.",
            "",
            "ARCHIVE LORE PREVIEW:",
            f"{ITALIC}{GRAY}{random.choice(LORE_DATABASE)}{RESET}"
        ]
        Renderer.draw_screen(" CYBERSPACE BREACH ENGINE ", main_lines, hud_lines=hud, side_box_title=" DECRYPT LOGS ", side_box_lines=side_lines)

    def draw_vendor(self):
        hud = Renderer.draw_hud(self.player)
        main_lines = [
            f"Welcome to Vendor terminal: {BOLD}{YELLOW}CYBERWARE OUTPOST{RESET}",
            "Available credits: " + YELLOW + f"₵{self.player.credits}" + RESET,
            "",
            "ITEMS FOR PURCHASE:"
        ]
        for idx, item in enumerate(self.vendor_inventory):
            if item.get("type") == "weapon":
                detail = f"Dmg: {item['damage']}"
            elif item.get("type") == "armor":
                detail = f"Def: {item['defense']}"
            else:
                detail = f"Heal/RAM: {item.get('heal', 0)}/{item.get('ram_restore', 0)}"
            main_lines.append(f"  [{idx}] {item['name']} - {CYAN}{detail}{RESET} | Cost: {YELLOW}₵{item['cost']}{RESET}")
        
        main_lines.append("")
        main_lines.append("Press the item number [0-8] to buy, or [Q]/[Esc] to exit merchant mode.")

        side_lines = [
            "--- YOUR WEAPON ---",
            f"{self.player.weapon['name']} (Dmg: {self.player.weapon['damage']})",
            "",
            "--- YOUR ARMOR ---",
            f"{self.player.armor['name']} (Def: {self.player.armor['defense']})"
        ]
        Renderer.draw_screen(" MERCHANT SUB-GRID ", main_lines, hud_lines=hud, side_box_title=" CURRENT GEAR ", side_box_lines=side_lines)

    def draw_inventory(self):
        hud = Renderer.draw_hud(self.player)
        main_lines = [
            "--- PERSONAL CARGO GRID ---",
            ""
        ]
        if not self.player.inventory:
            main_lines.append("Inventory is empty.")
        else:
            for idx, item in enumerate(self.player.inventory):
                t_str = item.get("type", "unknown").upper()
                main_lines.append(f"  [{idx}] {item['name']} ({t_str}) - {GRAY}{item.get('description', '')}{RESET}")
                
        main_lines.append("")
        main_lines.append("Press item number to Equip/Use. Press [Q]/[Esc] to close inventory.")

        side_lines = [
            "--- CURRENT GEAR ---",
            f"Weapon: {self.player.weapon['name']}",
            f"Armor:  {self.player.armor['name']}",
            "",
            "--- NET PROGRAMS ---",
        ]
        for prog in self.player.programs:
            side_lines.append(f"- {prog['name']}")

        Renderer.draw_screen(" CARGO BAY ", main_lines, hud_lines=hud, side_box_title=" INTEGRATED GEAR ", side_box_lines=side_lines)

    def draw_stats(self):
        hud = Renderer.draw_hud(self.player)
        main_lines = [
            f"--- HARDWARE SPECIFICATIONS FOR AGENT: {self.player.name} ---",
            "",
            f"  Current Level:       {BOLD}{GREEN}{self.player.level}{RESET}",
            f"  Experience Points:   {self.player.xp} / {self.player.xp_to_next}",
            f"  Max Structural integrity (HP): {self.player.max_hp}",
            f"  Max Processing Buffer (RAM):   {self.player.max_ram}",
            f"  Available Credits:   ₵{self.player.credits}",
            "",
            "Active Deck Modules Loaded:",
            f"  Cyberdeck Model:     {CYAN}{self.player.cyberdeck['name']}{RESET}",
            f"  Expansion Slots:     {self.player.cyberdeck['slots']}",
            f"  Extra RAM Buffer:    +{self.player.cyberdeck['ram_bonus']}",
            "",
            "Press [Q]/[Esc] to return to map exploration."
        ]
        Renderer.draw_screen(" AGENT DIAGNOSTICS CORE ", main_lines, hud_lines=hud)

    def draw_gameover(self):
        lines = [
            "",
            f"       {BOLD}{RED}███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗    ███████╗ █████╗ ██╗██╗     {RESET}",
            f"       {BOLD}{RED}████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗██║██║     {RESET}",
            f"       {BOLD}{RED}██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║    █████╗  ███████║██║██║     {RESET}",
            f"       {BOLD}{RED}██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║    ██╔══╝  ██╔══██║██║██║     {RESET}",
            f"       {BOLD}{RED}██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║    ██║     ██║  ██║██║███████╗{RESET}",
            f"       {RESET}{DIM}{RED}╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝{RESET}",
            "",
            "                           Agent vital signals terminated.",
            "",
            "                           [R] Reboot Simulator",
            "                           [Q] Exit to OS",
            ""
        ]
        Renderer.draw_screen(" SYSTEM BREACHED ", lines)

    def handle_input(self, key):
        if self.state == "MAIN_MENU":
            if key == "n":
                # Start game
                self.start_new_game("Neo")
            elif key == "q":
                self.running = False
                
        elif self.state == "EXPLORE":
            dx, dy = 0, 0
            if key == "w": dy = -1
            elif key == "s": dy = 1
            elif key == "a": dx = -1
            elif key == "d": dx = 1
            elif key == "q":
                self.state = "MAIN_MENU"
                return
            elif key == "i":
                self.state = "INVENTORY"
                return
            elif key == "c":
                self.state = "STATS"
                return
            
            if dx != 0 or dy != 0:
                nx = self.player.x + dx
                ny = self.player.y + dy
                
                # Check interaction first
                act_type, act_data = self.world.trigger_interaction(nx, ny, self.player)
                
                if act_type == "combat":
                    enemy_obj = Enemy(
                        name=act_data["name"],
                        hp=act_data["hp"],
                        max_hp=act_data["max_hp"],
                        level=act_data["level"],
                        damage=act_data["damage"],
                        xp_reward=act_data["xp_reward"],
                        credits_reward=act_data["credits_reward"],
                        x=nx,
                        y=ny
                    )
                    self.current_combat = Combat(self.player, enemy_obj)
                    self.state = "COMBAT"
                elif act_type == "hack":
                    self.current_hacking = HackingGame(self.player, difficulty=self.level_depth)
                    self.state = "HACKING"
                    self.active_terminal_pos = act_data
                elif act_type == "vendor":
                    self.state = "VENDOR"
                elif act_type == "exit":
                    self.level_depth += 1
                    self.load_level()
                elif self.world.is_walkable(nx, ny):
                    self.player.x = nx
                    self.player.y = ny

        elif self.state == "COMBAT":
            if key == "1":
                self.current_combat.player_attack()
                self.check_combat_resolution()
            elif key == "2":
                # For simplicity, trigger first hack module
                self.current_combat.player_hack(0)
                self.check_combat_resolution()
            elif key == "3":
                # Try to use first consumable in inventory
                idx = -1
                for i, item in enumerate(self.player.inventory):
                    if item.get("type") == "consumable":
                        idx = i
                        break
                if idx != -1:
                    self.current_combat.player_use_item(idx)
                    self.check_combat_resolution()
                else:
                    self.current_combat.add_log("No usable injectors in inventory!")
            elif key == "4":
                self.current_combat.player_flee()
                self.check_combat_resolution()

        elif self.state == "HACKING":
            if key in ("w", "s", "a", "d"):
                self.current_hacking.move_cursor(key)
            elif key == "\r" or key == "\n":
                res = self.current_hacking.select_cell()
                if res:
                    self.add_log(res)
                if self.current_hacking.completed:
                    self.world.remove_terminal(*self.active_terminal_pos)
                    self.state = "EXPLORE"
                elif self.current_hacking.failed:
                    self.world.remove_terminal(*self.active_terminal_pos)
                    self.state = "EXPLORE"
            elif key == "q":
                self.state = "EXPLORE"

        elif self.state == "VENDOR":
            if key in ("q", "\x1b"): # q or Esc
                self.state = "EXPLORE"
            elif key.isdigit():
                idx = int(key)
                if 0 <= idx < len(self.vendor_inventory):
                    purchased = self.vendor_inventory[idx]
                    if self.player.credits >= purchased["cost"]:
                        self.player.credits -= purchased["cost"]
                        self.player.add_item(purchased)
                        self.vendor_inventory.pop(idx)
                        self.add_log(f"Purchased: {purchased['name']} for ₵{purchased['cost']}.")
                    else:
                        self.add_log("Insufficient credits to complete purchase!")

        elif self.state == "INVENTORY":
            if key in ("q", "\x1b"):
                self.state = "EXPLORE"
            elif key.isdigit():
                idx = int(key)
                if 0 <= idx < len(self.player.inventory):
                    item = self.player.inventory[idx]
                    if item.get("type") == "weapon":
                        self.player.equip_weapon(item)
                        self.player.inventory.pop(idx)
                        self.add_log(f"Equipped weapon: {item['name']}")
                    elif item.get("type") == "armor":
                        self.player.equip_armor(item)
                        self.player.inventory.pop(idx)
                        self.add_log(f"Equipped armor: {item['name']}")
                    elif item.get("type") == "consumable":
                        heal = item.get("heal", 0)
                        self.player.hp = min(self.player.max_hp, self.player.hp + heal)
                        self.player.inventory.pop(idx)
                        self.add_log(f"Used consumable: {item['name']}. Healed {heal} HP.")
                        self.state = "EXPLORE"

        elif self.state == "STATS":
            if key in ("q", "\x1b"):
                self.state = "EXPLORE"

        elif self.state == "GAMEOVER":
            if key == "r":
                self.start_new_game("Neo")
            elif key == "q":
                self.running = False

    def check_combat_resolution(self):
        if not self.current_combat.is_active:
            if self.current_combat.victory:
                self.world.remove_enemy(self.current_combat.enemy)
                self.state = "EXPLORE"
            else:
                if not self.player.is_alive:
                    self.state = "GAMEOVER"
                else:
                    self.state = "EXPLORE" # Fled
            self.current_combat = None
            
    def shutdown(self):
        Renderer.restore_terminal()
