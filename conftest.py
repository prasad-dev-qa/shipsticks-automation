

# conftest.py
import pytest
from datetime import datetime
import os
import logging


# Ensure reports folder exists BEFORE logging config
if not os.path.exists("reports"):
    os.makedirs("reports")


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler('reports/test_log.log')  # Log to file
    ]
)

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": None
    }

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "args": ["--start-maximized"]
    }

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Ensure reports folder exists
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    if not config.pluginmanager.hasplugin("html"):
        return    

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join("reports", f"reg_{timestamp}.html")

    config.option.htmlpath = report_file
    config.option.self_contained_html = True

    print(f"Console Log - HTML Report created: {report_file}")