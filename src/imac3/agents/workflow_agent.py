"""
IMAC3 AI Workflow Agent

Public Demonstration Module
"""


class WorkflowAgent:

    def __init__(self, name="IMAC3 Workflow Agent"):
        self.name = name
        self.status = "READY"

    def run_workflow(self, workflow):

        return {
            "agent": self.name,
            "workflow": workflow,
            "status": "workflow completed"
        }

    def info(self):

        return {
            "name": self.name,
            "type": "workflow automation agent",
            "status": self.status
        }
