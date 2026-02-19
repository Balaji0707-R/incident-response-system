from utils.logger import log

class RiskValidationAgent:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        log("Risk Validation Agent Started")

        fix_plan = self.memory.get("fix_plan", [])
        risks = []

        for fix in fix_plan:
            if fix["risk"] == "Medium":
                risks.append("Rollback may remove newly deployed features")
            if fix["risk"] == "High":
                risks.append("Service restart may cause downtime")

        self.memory.set("risk_assessment", risks)

        log("Risk Validation Agent Completed")

        return risks
