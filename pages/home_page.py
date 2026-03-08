from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page
from config.constants import BASE_URL
import logging

logger = logging.getLogger(__name__)

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = BASE_URL
        self.textbox_where_from = self.page.get_by_placeholder("Where from")
        self.textbox_where_to = self.page.get_by_placeholder("Where to")
        self.button_trip_type = self.page.locator("button[aria-haspopup='listbox']")
        self.suggestion_selector = "div.flex.items-start.justify-start:not(.hidden)"
        self.address_suggestion_locator = self.page.locator("div.flex.items-start.justify-start:not(.hidden)")
        self.dropdown_trip_options_selector = self.page.locator("div.listboxoptions span")
        self.button_getstarted = self.page.get_by_role("button", name="Get started")

    def navigate(self):
        self.page.goto(self.url)
        logger.info(f"Navigated to : {self.url}")
     

    def _select_suggestion(self, pick_text: str | None = None):
        """Helper method to select a suggestion from the dropdown.
        
        Waits for suggestions to appear, then clicks the matching text or the first one.
        """
        self.page.wait_for_selector(self.suggestion_selector)
        if pick_text:
            self.address_suggestion_locator.get_by_text(pick_text, exact=True).click()
        else:
            self.address_suggestion_locator.first.click()

    def fill_origin(self, address: str):
        """Type an address into the origin field and choose a suggestion.        
        Args: address: The address string to type.
        """
        self.textbox_where_from.type(address)
        self._select_suggestion(address)
        logger.info(f"Origin Address filled: {address}")
        

    def fill_destination(self, address: str):
        """Type an address into the destination field and choose a suggestion.
        
        Args: address: The address string to type.
        """
        self.textbox_where_to.type(address)
        self._select_suggestion(address)
        logger.info(f"Destination Address filled: {address}")

    def select_trip_type(self, trip_type: str = "One way"):
        """Select the trip type from the dropdown.
        
        Args:
            trip_type: The trip type to select (e.g., "One way", "Round trip").
        """
        logger.info(f"Selecting trip type: {trip_type}")
        self.button_trip_type.click()
        self.dropdown_trip_options_selector.get_by_text(trip_type).click()
        logger.info(f"Trip type '{trip_type}' selected")
        

    def click_get_started(self):
        """Click the 'Get started' button to proceed."""
        self.button_getstarted.click()
        logger.info("'Get started' button clicked")
       

    def fill_address(self, origin: str, destination: str):
        """Convenience method to fill both origin and destination addresses.
        
        Args:
            origin: The origin address string to type.
            origin_pick: Specific suggestion text to select for origin; if None, selects the first.
            destination: The destination address string to type.
            destination_pick: Specific suggestion text to select for destination; if None, selects the first.
        """
        self.fill_origin(origin)
        self.fill_destination(destination)

    def start_booking(self, origin: str, destination: str, trip_type: str = "One way"):
        """Convenience method to perform the entire booking start flow.
        
        Args:
            origin: The origin address string to type.
            destination: The destination address string to type.
            trip_type: The trip type to select (e.g., "One way", "Round trip").
        """
        logger.info(f"Starting booking with Origin: {origin}, Destination: {destination}, Trip Type: {trip_type}")
        self.fill_address(origin, destination)
        self.select_trip_type(trip_type)
        self.click_get_started()



