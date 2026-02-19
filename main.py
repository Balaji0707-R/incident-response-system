import json
from memory.shared_memory import SharedMemory
from tools.log_analyzer_tool import LogAnalyzerTool
from tools.metrics_parser_tool import MetricsParserTool
from agents.detection_agent import IncidentDetectionAgent
from agents.rca_agent import RootCauseAnalysisAgent
from agents.fix_strategy_agent import FixStrategyAgent
from agents.risk_validation_agent import RiskValidationAgent
from agents.report_generator_agent import IncidentReportGeneratorAgent
from orchestrator.coordination_manager import CoordinationManager
from orchestrator.supervisor import Supervisor
from utils.json_parser import to_pretty_json

memory = SharedMemory()

memory.set("logs", open("sample_inputs/logs.txt").read())
memory.set("metrics", json.load(open("sample_inputs/metrics.json")))
memory.set("deployment_notes", open("sample_inputs/deployment_notes.txt").read())
memory.set("user_complaint", open("sample_inputs/user_complaint.txt").read())

agents = [
    IncidentDetectionAgent(memory, LogAnalyzerTool(), MetricsParserTool()),
    RootCauseAnalysisAgent(memory),
    FixStrategyAgent(memory),
    RiskValidationAgent(memory),
    IncidentReportGeneratorAgent(memory)
]

coordinator = CoordinationManager(agents)
supervisor = Supervisor(coordinator)
supervisor.run()

final_output = {
    "incident_severity": memory.get("incident_severity"),
    "probable_root_cause": memory.get("probable_root_cause"),
    "fix_plan": memory.get("fix_plan"),
    "risk_assessment": memory.get("risk_assessment"),
    "final_resolution": "DB connection pool increased and system stabilized",
    "incident_report": memory.get("incident_report")
}

print(to_pretty_json(final_output))
