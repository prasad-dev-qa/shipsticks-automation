from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.ship_page import ShipPage
import logging
from utilities.data_manager import DataManager

logger = logging.getLogger(__name__)

def test_ship_sticks_booking_step_1_happy_path(page: Page):
    """
    Validates the 'Step 1' booking flow for a one-way golf bag shipment.
    Ensures addresses are correctly filled and displayed on the shipping page.
    """
    logger.info("Starting test: test_ship_sticks_booking_step_1_happy_path")
    
    # Arrange: Set up page objects and test data
    home_page = HomePage(page)
    ship_page = ShipPage(page)
    
    # Act: Perform the booking steps
    home_page.navigate()
    home_page.start_booking(DataManager.origin, DataManager.destination, DataManager.trip_type)
    
   # Retrieve displayed addresses
    actual_origin = ship_page.get_shipping_origin()
    actual_destination = ship_page.get_shipping_destination()
      
     # Assert: Verify the addresses match expectations
    assert actual_origin in DataManager.origin, f"Expected '{DataManager.origin}' to contain '{actual_origin}'"
    logger.info(f"Origin assertion passed: '{actual_origin}' is in '{DataManager.origin}'")  # Console log for origin assertion
    assert actual_destination in DataManager.destination, f"Expected '{DataManager.destination}' to contain '{actual_destination}'"
    logger.info(f"Destination assertion passed: '{actual_destination}' is in '{DataManager.destination}'")  # Console log for destination assertion

    ship_page.enter_shipping_details(DataManager.delivery_date)  # Enter shipping details (e.g., increase golf bags count, select shipping option, select date)
   
    # Retrieve shipment cities from order summary
    shipment_cities = ship_page.get_shipment_cities()
   
    # Assert shipment cities (update expected values as needed)
    expected_cities = [DataManager.origin_city, DataManager.destination_city]  # Example; replace with actual expected cities
    expect(ship_page.shipment_cities).to_have_text(expected_cities)
    logger.info(f"Shipment Cities from order summary assertion passed : {shipment_cities}")  # Console log for shipment cities

    # Retrieve payment summary items
    payment_items = ship_page.get_payment_summary_items()
   
    # Assert payment summary items (update expected values as needed)
    expected_payment_items = [DataManager.item_name, DataManager.item_price]  # Example; replace with actual expected texts
    assert payment_items == expected_payment_items, f"Expected {expected_payment_items}, got {payment_items}"
    logger.info(f"Payment summary items assertion passed: {payment_items}")  # Console log for payment summary items
    
    # Retrieve total price
    total_price = ship_page.get_total_price()
     
    # Assert total price
    expected_price = DataManager.item_price  # Update with actual expected price
    expect(ship_page.price_element).to_have_text(expected_price)
    logger.info(f"Total price assertion passed: {total_price}")  # Console log for total price

    ship_page.complete_step1_booking()

     # Verify check-circle icon is visible
    expect(ship_page.checked_icon).to_be_visible()
    logger.info("Step 1 booking completed green Checked icon visibility assertion passed")  # Console log for checked icon visibility
    logger.info("Step 1 booking flow completed successfully")  # Console log for test completion
    logger.info("Test completed successfully")
    