import subprocess

class NetworkAgent:

    async def analyze(self, data):

        result = {}

        try:
            ping = subprocess.check_output(
                "ping 8.8.8.8 -n 1",
                shell=True,
                text=True
            )

            result["internet"] = "success"
            result["ping"] = ping

        except:
            result["internet"] = "failed"

        tun_mode = data.get("tun_mode", False)

        if tun_mode:
            result["tun"] = "enabled"

        dns = data.get("dns", "system")
        result["dns"] = dns

        if dns == "fake-ip":
            result["warning"] = "Possible FakeDNS conflict"

        return result
