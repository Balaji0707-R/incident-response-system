from utils.logger import log

class IncidentDetectionAgent:
    def __init__(self, memory, log_tool, metrics_tool):
        self.memory = memory
        self.log_tool = log_tool
        self.metrics_tool = metrics_tool

    def run(self):
        log("Detection Agent Started")

        logs = self.memory.get("logs")
        metrics = self.memory.get("metrics")

        log_result = self.log_tool.analyze(logs)
        metric_result = self.metrics_tool.parse(metrics)

        severity = "Low"

        if log_result["repeated_failures"] and metric_result["cpu_spike"]:
            severity = "Critical"
        elif log_result["repeated_failures"]:
            severity = "High"
        elif metric_result["high_latency"]:
            severity = "Medium"

        self.memory.set("incident_severity", severity)

        log(f"Detection Agent Completed: Severity = {severity}")

        return severity
