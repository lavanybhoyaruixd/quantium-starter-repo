import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Patch webdriver.Chrome to use webdriver-manager
_original_chrome_init = webdriver.Chrome.__init__


def _patched_chrome_init(self, options=None, service=None, **kwargs):
    if service is None:
        service = ChromeService(ChromeDriverManager().install())
    _original_chrome_init(self, options=options, service=service, **kwargs)


webdriver.Chrome.__init__ = _patched_chrome_init


def pytest_setup_options():
    """Configure Chrome options for Dash tests."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return options
