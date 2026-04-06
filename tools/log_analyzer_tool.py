class LogAnalyzerTool:
    def analyze(self, logs: str):
        logs_lower = logs.lower()

        return {
            "error_count": logs_lower.count("error"),
            "timeout_count": logs_lower.count("timeout"),
            "repeated_failures": logs_lower.count("error") >= 3
        }
