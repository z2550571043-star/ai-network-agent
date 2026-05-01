import json

class ConfigAgent:

    async def analyze(self, data):

        config_path = data.get("config")

        if not config_path:
            return {
                "status": "no config"
            }

        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        result = {
            "outbounds": len(config.get("outbounds", [])),
            "inbounds": len(config.get("inbounds", []))
        }

        dns = config.get("dns", {})

        if dns.get("strategy") == "prefer_ipv6":
            result["risk"] = "IPv6 may cause TUN issues"

        return result
