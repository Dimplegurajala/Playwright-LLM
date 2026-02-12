import pytest
import logging
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from models.ai_healer import AIHealer

@pytest.fixture(scope="session", autouse= True)
def logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    return logging.getLogger("QA_Ecosystem")

@pytest.fixture(scope="function")
def page(logger):
    with sync_playwright() as p:
        is_ci = os.getenv("CI", "false").lower() == "true"
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
    
        browser = p.chromium.launch(headless=is_ci)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources= True)
        page= context.new_page()
        yield page
        test_name = os.getenv('PYTEST_CURRENT_TEST', 'test').split(' ')[0].replace("::", "_")
        trace_path = f"outputs/trace_{test_name}.zip"
        context.tracing.stop(path=trace_path)
        browser.close()
    
@pytest.fixture(scope="function")
def healer():
    return AIHealer()


