from utils.logger import log

class FixStrategyAgent:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        log("Fix Strategy Agent Started")

        fix_plan = [
            {"action": "Increase DB connection pool size", "risk": "Low"},
            {"action": "Rollback latest deployment", "risk": "Medium"},
            {"action": "Restart affected services", "risk": "High"}
        ]

        self.memory.set("fix_plan", fix_plan)

        log("Fix Strategy Agent Completed")

        return fix_plan
