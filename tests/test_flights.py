import json
import pytest
from playwright.sync_api import sync_playwright
from page.flight_page import FlightPage
from utils.logger import get_logger

logger = get_logger()

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_flight_search(browser):
    page = browser.new_page()
    flight_page = FlightPage(page)

    try:
        logger.info("Opening site")
        flight_page.load()

        logger.info("Searching flights")
        flight_page.search_flights("Boston", "London")

        logger.info("Fetching results")
        flights = flight_page.get_results()

        assert len(flights) > 0

        with open("data/flights.json", "w") as f:
            json.dump(flights, f, indent=4)

        logger.info("Data saved successfully")

    except Exception as e:
        page.screenshot(path="screenshots/error_{int(time.time())}.png")
        logger.error(f"Test failed: {e}")
        raise