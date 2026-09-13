from src.imac3.core.engine import IMAC3Engine
from src.imac3.agents.base_agent import BaseAgent


def main():
    engine = IMAC3Engine()

    agent = BaseAgent("IMAC3 Demo Agent")

    print("=== IMAC3 AI Demo ===")
    print(engine.status())
    print(agent.run())


if __name__ == "__main__":
    main()
