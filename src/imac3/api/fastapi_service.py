"""
IMAC3 AI FastAPI Service
Public Demo API
"""

from fastapi import FastAPI

from src.imac3.core.intelligence_engine import IntelligenceEngine
from src.imac3.core.decision_engine import DecisionEngine
from src.imac3.agents.ai_agent import AIAgent


app = FastAPI(
    title="IMAC3 AI Platform",
    description="Intelligent Agent & AI Systems Demo",
    version="0.1.0"
)


engine = IntelligenceEngine()
decision = DecisionEngine()
agent = AIAgent()


@app.get("/")
def home():
    return {
        "system": "IMAC3 AI",
        "status": "ONLINE",
        "platform": "AI Agent Infrastructure"
    }


@app.get("/system")
def system_status():
    return engine.system_info()


@app.get("/agent")
def agent_status():
    return agent.execute(
        "Intelligent task processing"
    )


@app.get("/decision")
def decision_status():
    return decision.analyze(
        "Business operation data"
    )
