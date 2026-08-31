import random

class Entity:
    def __init__(self, name, hp, max_hp, level, x=0, y=0):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.level = level
        self.x = x
        self.y = y

    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
        return amount


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 100, 1, 0, 0)
        self.ram = 10
        self.max_ram = 10
        self.credits = 500
        self.xp = 0
        self.xp_to_next = 100
        
        # Equipped Gear
        self.weapon = {
            "name": "Mono-Wire",
            "type": "weapon",
            "damage": 12,
            "cost": 0,
            "description": "Standard neural mono-filament wire. Swift and clean."
        }
        self.armor = {
            "name": "Polycarbonate Jacket",
            "type": "armor",
            "defense": 2,
            "description": "Basic street-grade protective gear."
        }
        self.cyberdeck = {
            "name": "Fuchi v1 Cyberdeck",
            "type": "cyberdeck",
            "slots": 3,
            "ram_bonus": 2
        }

        # Inventories
        self.inventory = []
        self.programs = [
            {"name": "ShortCircuit.exe", "type": "program", "ram_cost": 3, "damage": 20, "desc": "Zap neural circuits for electric damage."},
            {"name": "Overheat.exe", "type": "program", "ram_cost": 4, "damage": 30, "desc": "Burn synthetic nervous systems."}
        ]

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_name):
        for item in self.inventory:
            if item["name"].lower() == item_name.lower():
                self.inventory.remove(item)
                return item
        return None

    def equip_weapon(self, weapon):
        if self.weapon["name"] != "Mono-Wire":
            self.add_item(self.weapon)
        self.weapon = weapon

    def equip_armor(self, armor):
        if self.armor["name"] != "Polycarbonate Jacket":
            self.add_item(self.armor)
        self.armor = armor

    def gain_xp(self, amount):
        self.xp += amount
        leveled_up = False
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level += 1
            self.max_hp += 20
            self.hp = self.max_hp
            self.max_ram += 2
            self.ram = self.max_ram
            self.xp_to_next = int(self.xp_to_next * 1.5)
            leveled_up = True
        return leveled_up


class Enemy(Entity):
    def __init__(self, name, hp, max_hp, level, damage, xp_reward, credits_reward, x=0, y=0):
        super().__init__(name, hp, max_hp, level, x, y)
        self.damage = damage
        self.xp_reward = xp_reward
        self.credits_reward = credits_reward

    def attack(self, target):
        damage_roll = int(self.damage * random.uniform(0.8, 1.2))
        final_damage = max(1, damage_roll - target.armor.get("defense", 0))
        target.take_damage(final_damage)
        return final_damage


class Vendor:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def sell_item(self, player, item_index):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if player.credits >= item["cost"]:
                player.credits -= item["cost"]
                player.add_item(item)
                # Keep items infinite or remove
                return item
        return None
