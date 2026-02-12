class ResilienceManager:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger
    
    def monitor_network(self):
        def handle_route(route):
            try:
                response = route.fetch()
                if response.status >= 400:
                    level = "CRITICAL" if response.status >= 500 else "ERROR"
                    self.logger.log(100, f"Cloud API Error: {route.request.url} returned {response.status}")
                route.fulfill(response=response)
            except Exception:
                route.continue_()

        self.page.route("**/*", handle_route)