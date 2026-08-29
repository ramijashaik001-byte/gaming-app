# CyberArcade & NeonRogue

Welcome to **CyberArcade**, a premium web-based retro game hub featuring three fully playable interactive arcade games (Neon Snake, Space Defenders, and Cyber Breakout), served via a custom python web server. This package also includes **NeonRogue**, a highly immersive console text-based terminal RPG written in Python with procedural dungeon mapping and a cyberspace breach hacking minigame.

---

## Features

* **CyberArcade (Web Hub)**:
  * **Neon Snake**: Dynamic grid movement with glowing speed boosts and particle explosions.
  * **Space Defenders**: Top-down shooter with player shield metrics and enemy invader rows.
  * **Cyber Breakout**: Paddle deflection physics with bouncing velocity adjustments.
  * **High-Score Persistence**: Top player initials and score metrics saved locally in a JSON file.
  * **Audio Synthesizer**: Custom sound effects synthesized directly using the Web Audio API.

* **NeonRogue (Terminal RPG)**:
  * Turn-based melee combat loop.
  * Cyberspace Breach Hacking minigame.
  * Procedural level generation.
  * Custom ANSI terminal UI screens.

---

## Dependencies

* **Python 3.12+**
* **Node.js (for package package-lock verification)**

No external library dependencies are required! Both the console game and localhost web server run natively using standard library components.

---

## Installation

Clone or extract the repository files:
```bash
git clone <repository-url>
cd "gaming app"
```

Install node dependencies (verifies package manifests):
```bash
npm install
```

---

## Running the Web Game Hub (Localhost)

1. Start the Python web server in the directory root:
   ```bash
   python server.py
   ```
2. Open your web browser and navigate to:
   **[http://localhost:8000](http://localhost:8000)**

---

## Running the Terminal RPG (Console)

To play the console-based text RPG, execute the launcher in PowerShell or Command Prompt:
```bash
python main.py
```
*(Use `W`/`A`/`S`/`D` to move, `I` for inventory, `C` for character diagnostics, `H` to breach terminals, and `V` to purchase equipment).*

---

## Running Automated Tests

To execute the game system unit tests, run:
```bash
python -m unittest discover -s tests -p "test_*.py"
```


