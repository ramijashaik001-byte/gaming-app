import sys
from engine.core import GameEngine

def main():
    engine = GameEngine()
    try:
        engine.run()
    except KeyboardInterrupt:
        pass
    finally:
        engine.shutdown()

if __name__ == "__main__":
    main()
