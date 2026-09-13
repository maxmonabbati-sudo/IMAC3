"""
IMAC3 AI FastAPI Platform

Public Product Demo
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from dashboard.dashboard_demo import dashboard_page

from src.imac3.core.intelligence_engine import IntelligenceEngine
from src.imac3.core.decision_engine import DecisionEngine
from src.imac3.agents.ai_agent import AIAgent
from src.imac3.automation.workflow_manager import WorkflowManager
from src.imac3.data.intelligence_layer import IntelligenceDataLayer


app = FastAPI(
    title="IMAC3 AI Platform",
    description="Intelligent Agent & AI Infrastructure Demo",
    version="0.1.0"
)


engine = IntelligenceEngine()
decision = DecisionEngine()
agent = AIAgent()
workflow = WorkflowManager()
data_layer = IntelligenceDataLayer()


@app.get("/", response_class=HTMLResponse)
def dashboard():

    return dashboard_page()


@app.get("/api/status")
def status():

    return {
        "system": "IMAC3 AI",
        "status": "ONLINE",
        "version": "0.1.0"
    }


@app.get("/api/agent")
def agent_status():

    return agent.execute(
        "Intelligent task processing"
    )


@app.get("/api/decision")
def decision_status():

    return decision.analyze(
        "Business intelligence data"
    )


@app.get("/api/automation")
def automation_status():

    return workflow.execute(
        "Enterprise workflow"
    )


@app.get("/api/data")
def data_status():

    return data_layer.analyze(
        "AI data layer"
    )
