from agents.network_agent import NetworkAgent
from agents.config_agent import ConfigAgent
from agents.browser_agent import BrowserAgent
from agents.repair_agent import RepairAgent

class CoordinatorAgent:

    def __init__(self):
        self.network_agent = NetworkAgent()
        self.config_agent = ConfigAgent()
        self.browser_agent = BrowserAgent()
        self.repair_agent = RepairAgent()

    async def run(self, data):

        network_result = await self.network_agent.analyze(data)
        config_result = await self.config_agent.analyze(data)
        browser_result = await self.browser_agent.analyze(data)

        repair_result = await self.repair_agent.fix(
            network_result,
            config_result,
            browser_result
        )

        return {
            "network": network_result,
            "config": config_result,
            "browser": browser_result,
            "repair": repair_result
        }
