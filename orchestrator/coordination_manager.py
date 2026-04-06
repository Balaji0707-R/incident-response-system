from utils.logger import log
from config import MAX_COORDINATION_ROUNDS

class CoordinationManager:
    def __init__(self, agents):
        self.agents = agents

    def run(self):
        log("Coordination Started")

        for round_number in range(MAX_COORDINATION_ROUNDS):
            log(f"Coordination Round {round_number + 1}")

            for agent in self.agents:
                agent.run()

            break  # Single coordinated execution

        log("Coordination Completed")
