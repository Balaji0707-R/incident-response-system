from utils.logger import log

class IncidentReportGeneratorAgent:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        log("Report Generator Agent Started")

        report = {
            "summary": "Critical incident caused by database timeouts after deployment",
            "timeline": [
                "Deployment completed",
                "Multiple DB timeout errors observed",
                "Severity escalated to Critical",
                "Fix implemented and system stabilized"
            ],
            "impact_analysis": "Users were unable to place orders and payments failed",
            "preventive_actions": [
                "Add database monitoring alerts",
                "Perform load testing before production deployment"
            ]
        }

        self.memory.set("incident_report", report)

        log("Report Generator Agent Completed")

        return report
