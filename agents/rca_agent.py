from utils.logger import log

class RootCauseAnalysisAgent:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        log("RCA Agent Started")

        logs = self.memory.get("logs")
        deployment = self.memory.get("deployment_notes")

        if "db" in logs.lower() and "timeout" in logs.lower():
            cause = "Database connection pool exhaustion after deployment"
            impacted = ["order-service", "payment-service"]
        else:
            cause = "Unknown root cause"
            impacted = []

        self.memory.set("probable_root_cause", cause)
        self.memory.set("impacted_services", impacted)

        log(f"RCA Agent Completed: Cause = {cause}")

        return cause
