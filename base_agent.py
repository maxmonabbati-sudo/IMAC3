"""
IMAC3 AI Agent Base
"""

class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self):
        return f"{self.name} active"


if __name__ == "__main__":
    agent = BaseAgent("IMAC3 Agent")
    print(agent.run())
