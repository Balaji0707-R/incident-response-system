from utils.logger import log

class Supervisor:
    def __init__(self, coordinator):
        self.coordinator = coordinator

    def run(self):
        log("Supervisor Started")
        self.coordinator.run()
        log("Supervisor Completed")
