class BaseAgent:

    def __init__(self, name):
        self.name = name

    def run(self):
        return f"{self.name} active"
