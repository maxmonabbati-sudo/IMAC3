"""
IMAC3 AI FastAPI Service

Public Demonstration API
"""

from fastapi import FastAPI

from src.imac3.core.intelligence_engine import IntelligenceEngine
from src.imac3.core.decision_engine import DecisionEngine
from src.imac3.agents.ai_agent import AIAgent
from src.imac3.automation.workflow_manager import WorkflowManager
from src.imac3.data.intelligence_layer import IntelligenceDataLayer


app = FastAPI(
    title="IMAC3 AI Platform",
    description="Intelligent Agent & AI Systems Demonstration",
    version="0.1.0"
)


engine = IntelligenceEngine()
decision = DecisionEngine()
agent = AIAgent()
workflow = WorkflowManager()
data_layer = IntelligenceDataLayer()


@app.get("/")
def home():

    return {
        "system": "IMAC3 AI",
        "status": "ONLINE",
        "platform": "Intelligent AI Infrastructure"
    }


@app.get("/system")
def system():

    return engine.system_info()


@app.get("/agent")
def agent_demo():

    return agent.execute(
        "AI task processing"
    )


@app.get("/decision")
def decision_demo():

    return decision.analyze(
        "Enterprise operation data"
    )


@app.get("/automation")
def automation_demo():

    return workflow.execute(
        "Business workflow"
    )


@app.get("/data")
def data_demo():

    return data_layer.analyze(
        "Demo intelligence data"
    )
