import os
import sys

# ANSI Escape Sequences
CLEAR = "\033[2J\033[H"
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Cyberpunk Neon Colors
PINK = "\033[38;5;198m"     # Neon pink / magenta
CYAN = "\033[38;5;51m"      # Neon cyan / light blue
GREEN = "\033[38;5;82m"     # Neon green
YELLOW = "\033[38;5;226m"   # Neon yellow
ORANGE = "\033[38;5;208m"   # Neon orange
PURPLE = "\033[38;5;99m"     # Deep purple
RED = "\033[38;5;196m"      # Alert red
GRAY = "\033[38;5;244m"     # Dark gray

# BG Colors
BG_DARK = "\033[48;5;232m"
BG_PINK = "\033[48;5;198m"
BG_CYAN = "\033[48;5;51m"

class Renderer:
    @staticmethod
    def init_terminal():
        """Initializes the terminal for ANSI escapes (required on older Windows cmd versions)."""
        if sys.platform == "win32":
            os.system("color")
        # Hide cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    @staticmethod
    def restore_terminal():
        """Restores the terminal cursor on exit."""
        sys.stdout.write("\033[?25h" + RESET + CLEAR)
        sys.stdout.flush()

    @staticmethod
    def clear():
        sys.stdout.write(CLEAR)
        sys.stdout.flush()

    @staticmethod
    def draw_box(width, height, title, content_lines, border_color=CYAN):
        """Draws a beautiful neon border box with content lines."""
        lines = []
        # Title border
        title_str = f" {title} " if title else ""
        border_top = "┌" + title_str.center(width - 2, "─") + "┐"
        lines.append(border_color + border_top + RESET)

        for i in range(height - 2):
            content = content_lines[i] if i < len(content_lines) else ""
            # Strip ANSI codes for length calculation
            clean_content = Renderer.strip_ansi(content)
            padding_len = max(0, width - 2 - len(clean_content))
            lines.append(border_color + "│ " + RESET + content + (" " * padding_len) + border_color + " │" + RESET)

        border_bottom = "└" + ("─" * (width - 2)) + "┘"
        lines.append(border_color + border_bottom + RESET)
        return lines

    @staticmethod
    def strip_ansi(text):
        """Removes ANSI escape codes to calculate string printable width correctly."""
        import re
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    @staticmethod
    def make_progress_bar(value, max_value, length, fill_char="█", empty_char="░", filled_color=GREEN, empty_color=GRAY):
        """Returns a string representing a progress bar."""
        if max_value <= 0:
            percent = 0
        else:
            percent = min(1.0, max(0.0, value / max_value))
        filled_len = int(round(length * percent))
        bar = filled_color + (fill_char * filled_len) + empty_color + (empty_char * (length - filled_len)) + RESET
        return f"{bar} {int(percent * 100)}%"

    @staticmethod
    def draw_hud(player):
        """Draws the HUD displaying Player Stats (Health, RAM, Credits, Level, XP)."""
        hud_lines = []
        name_str = f"{BOLD}{CYAN}AGENT: {player.name} [Lvl {player.level}]{RESET}"
        credits_str = f"{YELLOW}Credits: ₵{player.credits}{RESET}"
        hud_lines.append(f"{name_str} | {credits_str}")

        hp_bar = Renderer.make_progress_bar(player.hp, player.max_hp, 15, filled_color=RED)
        ram_bar = Renderer.make_progress_bar(player.ram, player.max_ram, 15, filled_color=CYAN)
        xp_bar = Renderer.make_progress_bar(player.xp, player.xp_to_next, 15, filled_color=PINK)

        hud_lines.append(f"HP:  {hp_bar}   RAM: {ram_bar}   XP:  {xp_bar}")
        return hud_lines

    @staticmethod
    def draw_screen(main_box_title, main_box_lines, hud_lines=None, side_box_title=None, side_box_lines=None):
        """Assembles a full-screen layout and prints it."""
        total_width = 110
        main_width = 75 if side_box_lines is not None else total_width
        side_width = total_width - main_width - 1

        main_box = Renderer.draw_box(main_width, 22, main_box_title, main_box_lines, border_color=CYAN)
        
        output = [CLEAR]
        if hud_lines:
            # Draw HUD
            output.append(f"{BOLD}{PINK}╔════════════════════════════════════════ NEON ROGUE HUD ═════════════════════════════════════════╗{RESET}")
            for line in hud_lines:
                output.append(f"║ {line:<107} ║")
            output.append(f"{BOLD}{PINK}╚═════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

        if side_box_lines is not None:
            side_box = Renderer.draw_box(side_width, 22, side_box_title, side_box_lines, border_color=PINK)
            for i in range(len(main_box)):
                output.append(main_box[i] + " " + side_box[i])
        else:
            for line in main_box:
                output.append(line)

        output.append("\n" + BOLD + PINK + "Controls: [WASD] Move/Explore | [I] Inventory | [H] Hack | [V] Vendor | [C] Stats | [Q] Quit" + RESET)
        
        # Flush output to console
        sys.stdout.write("\n".join(output) + "\n")
        sys.stdout.flush()
