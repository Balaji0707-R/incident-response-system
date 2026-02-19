class MetricsParserTool:
    def parse(self, metrics: dict):
        return {
            "cpu_spike": metrics.get("cpu_usage", 0) > 80,
            "high_latency": metrics.get("latency_ms", 0) > 1000
        }
