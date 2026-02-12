from pages.base_page import BasePage
from playwright.sync_api import sync_playwright, expect

class ContactListPage(BasePage):
    ADD_CONTACT_BTN = "#add-contact"
    
    def navigate_to_add_contact(self):
        self.click(self.ADD_CONTACT_BTN)

    def verify_contact_present(self, email):
        row = self.page.locator("tr", has_text=email)
        expect(row).to_be_visible(timeout=5000)