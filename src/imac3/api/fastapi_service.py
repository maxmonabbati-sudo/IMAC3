"""
IMAC3 AI FastAPI Platform

Public Product Demo API
"""

from fastapi import FastAPI

from src.imac3.config.settings import settings

from src.imac3.core.intelligence_engine import IntelligenceEngine
from src.imac3.core.decision_engine import DecisionEngine
from src.imac3.agents.ai_agent import AIAgent
from src.imac3.automation.workflow_manager import WorkflowManager
from src.imac3.data.intelligence_layer import IntelligenceDataLayer


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="IMAC3 AI Intelligent Agent Platform Demo"
)


engine = IntelligenceEngine()
decision = DecisionEngine()
agent = AIAgent()
workflow = WorkflowManager()
data_layer = IntelligenceDataLayer()


@app.get("/")
def home():

    return {
        "system": settings.app_name,
        "version": settings.version,
        "status": settings.api_status,
        "environment": settings.environment
    }


@app.get("/system")
def system_status():

    return engine.system_info()


@app.get("/agent")
def agent_status():

    return agent.execute(
        "AI intelligent task processing"
    )


@app.get("/decision")
def decision_status():

    return decision.analyze(
        "Business intelligence scenario"
    )


@app.get("/automation")
def automation_status():

    return workflow.execute(
        "Enterprise workflow"
    )


@app.get("/data")
def data_status():

    return data_layer.analyze(
        "Intelligent data layer"
    )


@app.get("/config")
def config_status():

    return settings.info()
