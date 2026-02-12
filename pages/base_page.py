from playwright.sync_api import sync_playwright, Page
from utils.resilience import ResilienceManager

class BasePage:
    def __init__(self, page: Page, healer, logger):
        self.page = page
        self.healer = healer
        self.logger = logger
        self.resilience = ResilienceManager(self.page, self.logger)
        self.resilience.monitor_network()

    def _execute_resiliently(self, selector, action_name, *args):
        try:
            element = self.page.locator(selector)
            getattr(element, action_name)(*args, timeout=3000)
        except Exception:
            self.logger.warning(f"'{action_name}' failed for {selector}. Healing...")
            fix = self.healer.suggest_fix(selector, self.page.content())
            if fix:
                target = self._map_semantic_locator(fix)
                getattr(target, action_name)(*args)
            else: raise

    def click(self, selector): self._execute_resiliently(selector, "click")
    def fill(self, selector, value): self._execute_resiliently(selector, "fill", value)

    def _map_semantic_locator(self, fix: dict):
        l_type, val, name = fix.get("type"), fix.get("value"), fix.get("name")
        if l_type == "role": return self.page.get_by_role(val, name=name)
        elif l_type == "label": return self.page.get_by_label(val)
        elif l_type == "placeholder": return self.page.get_by_placeholder(val)
        else: return self.page.get_by_text(val if val else name)