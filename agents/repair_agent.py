class RepairAgent:

    async def fix(self, network, config, browser):

        solutions = []

        if network.get("internet") == "failed":
            solutions.append("Check outbound proxy")

        if network.get("warning"):
            solutions.append(
                "Disable FakeDNS or switch to real DNS"
            )

        if config.get("risk"):
            solutions.append(
                "Disable prefer_ipv6 strategy"
            )

        if browser.get("tip"):
            solutions.append(browser["tip"])

        return {
            "solutions": solutions
        }
