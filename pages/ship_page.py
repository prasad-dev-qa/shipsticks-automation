from playwright.sync_api import Page, expect
import logging

from pytest_playwright.pytest_playwright import page

logger = logging.getLogger(__name__)

class ShipPage:
    def __init__(self, page: Page):
        self.page = page
        self.i_understand_button = page.get_by_role("button", name="I understand")
        self.shipping_options = page.locator("span.whitespace-nowrap.overflow-hidden.text-ellipsis")
        self.increase_golf_bags_button = page.get_by_role("button", name="Increase Golf Bags count")
        self.standard_shipping_button = page.locator("button").filter(has_text="Standard")
        self.select_date_button = page.get_by_role("button", name="Please select a date")
        self.date_arrow_button = page.locator("div.rdp-month.rdp-caption_start button.inline-flex  span.icon-arrow-right")
        self.ground_option = page.locator("//div[contains(@class, 'flex items-center justify-start bg-white')]/span[normalize-space()='Ground']")
        self.trip_type_header = page.locator("h4[aria-label='TripType']")
        self.shipment_cities = page.locator("div[aria-label='ShipmentCity']")
        
        self.shipping_label =  page.locator("//div[@aria-label='Shipping']")
        self.payment_summary = page.locator("div[aria-label='PaymentSummaryItem']")
        self.price_element = page.locator("strong.text-theme-accessibility.text-right div")
        self.next_traveler_button = page.locator("form div.md-max\\:transition-transform button").filter(has_text="Next: Traveler Details")
        self.checked_icon = page.locator("//form//div[contains(@class,'leading-none flex gap-2 items-center')]/span[contains(@class, 'icon-check-circle-filled')]")
       

    def click_i_understand(self):
        logger.info("Waiting for modal dialog and 'I understand' button")
        # Wait for the dialog modal to appear (wait for attached since it may be hidden initially)
        self.page.get_by_role("dialog").wait_for(state="attached", timeout=2000)
        self.i_understand_button.wait_for()
        logger.info("Clicking 'I understand' button")
        self.i_understand_button.click()
        logger.info("'I understand' button clicked")
                

    def get_shipping_origin(self):
        logger.info("Retrieving shipping origin address")
        origin = self.shipping_options.nth(0).text_content()
        logger.info(f"Shipping origin: {origin}")
        return origin
    
    def get_shipping_destination(self):
        logger.info("Retrieving shipping destination address")
        destination = self.shipping_options.nth(1).text_content()
        logger.info(f"Shipping destination: {destination}")
        return destination

    def increase_golf_bags_count(self):
        """Click the button to increase the golf bags count."""
        logger.info("Clicking 'Increase Golf Bags count' button")
          # Scroll to the standard shipping button to ensure visibility
        self.increase_golf_bags_button.click()
        logger.info("'Increase Golf Bags count' button clicked")        
        self.scroll_to_element(self.select_date_button)
        print("Clicked 'Increase Golf Bags count' button")

    def select_standard_shipping(self):
        """Click the 'Standard' shipping option button."""
        logger.info("Selecting 'Standard' shipping option")
        self.standard_shipping_button.click()
        logger.info("'Standard' shipping option selected")

    def click_select_date(self):
        """Click the 'Please select a date' button to open the date picker."""
        logger.info("Clicking 'Please select a date' button")
        self.select_date_button.click()
        logger.info("'Please select a date' button clicked")
        print("Clicked 'Please select a date' button")

    def click_date_arrow(self):
        """Click the arrow button in the date picker to navigate to the next month."""
        logger.info("Clicking date picker arrow button to navigate to next month")
        self.date_arrow_button.click()
        logger.info("Date picker arrow button clicked")
          # Wait for the calendar to update after clicking

    def select_ground_option(self):
        """Click the 'Ground' option."""
        logger.info("Selecting 'Ground' option")
        self.ground_option.click()
        logger.info("'Ground' option selected")

    def get_trip_type(self):
        """Get the text from the TripType header."""
        logger.info("Retrieving trip type text")
        trip_type = self.trip_type_header.text_content()
        logger.info(f"Trip type: {trip_type}")
        return trip_type

    def get_shipment_cities(self):
        """Get the texts from the ShipmentCity divs."""
        logger.info("Retrieving shipment cities texts")
        cities = self.shipment_cities.all_text_contents()
        logger.info(f"Shipment cities: {cities}")
        return cities

    def get_payment_summary_items(self):
        """Get the texts from the spans inside the PaymentSummaryItem div."""
        logger.info("Retrieving payment summary items")
        items = self.payment_summary.locator("span").all_text_contents()
        logger.info(f"Payment summary items: {items}")
        return items

    def get_total_price(self):
        """Get the text from the total price element."""
        logger.info("Retrieving total price")
        price = self.price_element.text_content()
        logger.info(f"Total price: {price}")
        return price

    def click_next_traveler_details(self):
        """Click the 'Next: Traveler Details' button."""
        logger.info("Clicking 'Next: Traveler Details' button")
        self.next_traveler_button.click()
        logger.info("'Next: Traveler Details' button clicked")

    def is_checked_icon_visible(self) -> bool:
        """Return True if the check-circle icon is visible."""
        visible = self.checked_icon.is_visible()
        logger.info(f"Checked icon visible: {visible}")
        return visible

    def scroll_to_element(self, locator):
        """Scroll the page so that the specified locator is in view."""
        logger.info(f"Scrolling to element: {locator}")
        locator.scroll_into_view_if_needed()
        logger.info("Element scrolled into view")

    def select_delivery_date(self, date_str: str):
        """Select a delivery date from the date picker.
        
        Args:
            date_str: The date string to select (e.g., "2024-07-15").
        """
        logger.info(f"Selecting delivery date: {date_str}")
        # Implement logic to select the date based on the provided string
        self.click_select_date()
        self.click_date_arrow()  # Navigate to the next month if needed (this is just an example, you may need more complex logic)
        self.page.get_by_label(date_str).click()
        self.scroll_to_element(self.ground_option)
        self.select_ground_option()
        logger.info(f"Delivery date '{date_str}' selected")
        print(f"Delivery date '{date_str}' selected")

    def click_shipping_label(self):
        """Click the 'Shipping' label to expand shipping details."""
        logger.info("Clicking 'Shipping' label")
        self.shipping_label.click()
        logger.info("'Shipping' label clicked")


    def enter_shipping_details(self, delivery_date: str):
        """Convenience method to enter shipping details and proceed.
        
        Args:
            delivery_date: The delivery date string to select.
        """
        self.click_i_understand()
        self.increase_golf_bags_count()
        self.select_delivery_date(delivery_date)
        self.click_shipping_label()  # Click to expand shipping details

    def complete_step1_booking(self):
        """Convenience method to complete all actions for step 1 booking. """
        self.click_next_traveler_details()
        
       
        