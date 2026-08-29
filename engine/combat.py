import random
from engine.renderer import BOLD, RED, RESET, GREEN, CYAN, YELLOW, GRAY, PINK

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.combat_log = [f"ENGAGED IN COMBAT WITH: {enemy.name} (Lvl {enemy.level})!"]
        self.is_active = True
        self.victory = False

    def add_log(self, text):
        self.combat_log.append(text)
        if len(self.combat_log) > 15:
            self.combat_log.pop(0)

    def player_attack(self):
        # Calculate physical damage
        dmg_base = self.player.weapon.get("damage", 10)
        dmg = int(dmg_base * random.uniform(0.9, 1.2))
        
        # Check crit chance
        crit = False
        if random.random() < 0.15:
            dmg = int(dmg * 1.5)
            crit = True

        actual_dmg = self.enemy.take_damage(dmg)
        
        crit_str = f"{BOLD}{RED}CRITICAL HIT!{RESET} " if crit else ""
        self.add_log(f"You strike {self.enemy.name} with your {self.player.weapon['name']} for {crit_str}{YELLOW}{actual_dmg} damage{RESET}.")
        
        if not self.enemy.is_alive:
            self.resolve_victory()
        else:
            self.enemy_turn()

    def player_hack(self, program_index):
        if program_index < 0 or program_index >= len(self.player.programs):
            self.add_log("Invalid hack index!")
            return

        prog = self.player.programs[program_index]
        if self.player.ram < prog["ram_cost"]:
            self.add_log(f"{RED}Not enough RAM! Need {prog['ram_cost']} RAM.{RESET}")
            return

        self.player.ram -= prog["ram_cost"]
        dmg = int(prog["damage"] * random.uniform(0.95, 1.1))
        actual_dmg = self.enemy.take_damage(dmg)
        
        self.add_log(f"Executed {CYAN}{prog['name']}{RESET} program. Siphoned {YELLOW}{actual_dmg} network damage{RESET} to {self.enemy.name}.")
        
        if not self.enemy.is_alive:
            self.resolve_victory()
        else:
            self.enemy_turn()

    def player_use_item(self, item_index):
        if item_index < 0 or item_index >= len(self.player.inventory):
            self.add_log("Invalid item index!")
            return

        item = self.player.inventory[item_index]
        if item.get("type") != "consumable":
            self.add_log("That item is not usable in combat.")
            return

        # Restore effect
        heal = item.get("heal", 0)
        ram_restore = item.get("ram_restore", 0)

        if heal > 0:
            self.player.hp = min(self.player.max_hp, self.player.hp + heal)
            self.add_log(f"Used {item['name']}. Restored {GREEN}{heal} HP{RESET}.")
        if ram_restore > 0:
            self.player.ram = min(self.player.max_ram, self.player.ram + ram_restore)
            self.add_log(f"Used {item['name']}. Restored {CYAN}{ram_restore} RAM{RESET}.")

        self.player.inventory.pop(item_index)
        self.enemy_turn()

    def player_flee(self):
        if random.random() < 0.4:
            self.add_log(f"{GREEN}Flee successful! You slip into the shadows.{RESET}")
            self.is_active = False
            self.victory = False
        else:
            self.add_log(f"{RED}Flee failed! The enemy blocks your escape.{RESET}")
            self.enemy_turn()

    def enemy_turn(self):
        if not self.enemy.is_alive:
            return
        
        # Enemy attacks player
        dmg = self.enemy.attack(self.player)
        self.add_log(f"{self.enemy.name} attacks you for {RED}{dmg} damage{RESET}.")

        if not self.player.is_alive:
            self.add_log(f"{BOLD}{RED}CRITICAL SYSTEM FAILURE! YOU DIED.{RESET}")
            self.is_active = False
            self.victory = False

    def resolve_victory(self):
        self.add_log(f"{BOLD}{GREEN}VICTORY! Enemy defeated.{RESET}")
        
        # Reward Player
        self.player.credits += self.enemy.credits_reward
        self.add_log(f"Retrieved {YELLOW}₵{self.enemy.credits_reward}{RESET} from enemy wreckage.")
        
        lvl_up = self.player.gain_xp(self.enemy.xp_reward)
        self.add_log(f"Gained {PINK}{self.enemy.xp_reward} XP{RESET}.")
        if lvl_up:
            self.add_log(f"{BOLD}{GREEN}▲ ▲ SYSTEM UPGRADED! You reached Level {self.player.level}! ▲ ▲{RESET}")

        self.is_active = False
        self.victory = True
