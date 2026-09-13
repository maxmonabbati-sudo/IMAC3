from src.imac3.core.intelligence_engine import IntelligenceEngine
from src.imac3.core.decision_engine import DecisionEngine


engine = IntelligenceEngine()
decision = DecisionEngine()


print(engine.system_info())


print(
    decision.analyze(
        "Enterprise operation scenario"
    )
)
