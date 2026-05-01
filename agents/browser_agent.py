class BrowserAgent:

    async def analyze(self, data):

        browser = data.get("browser", "chrome")

        result = {
            "browser": browser
        }

        if browser == "edge":
            result["warning"] = (
                "Edge may use system proxy directly"
            )

        input_method = data.get("input_method")

        if input_method == "microsoft":
            result["tip"] = (
                "Disable Bing cloud suggestion"
            )

        return result
