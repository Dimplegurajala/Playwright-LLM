from pages.base_page import BasePage

class AddContactPage(BasePage):
    FIRST_NAME = "#firstName"
    LAST_NAME = "#lastName"
    DOB = "#birthdate"
    EMAIL = "#email"
    PHONE = "#phone"
    STREET1 = "#street1"
    STREET2 = "#street2"
    CITY = "#city"
    STATE = "#stateProvince"
    POSTAL = "#postalCode"
    COUNTRY = "#country"
    SUBMIT_BTN = "#submit"

    def fill_contact_details(self, contact_data: dict):
        self.fill(self.FIRST_NAME, contact_data.get("first"))
        self.fill(self.LAST_NAME, contact_data.get("last"))
        self.fill(self.DOB, contact_data.get("dob"))
        self.fill(self.EMAIL, contact_data.get("email"))
        self.fill(self.PHONE, contact_data.get("phone"))
        self.fill(self.STREET1, contact_data.get("street1"))
        self.fill(self.STREET2, contact_data.get("street2"))
        self.fill(self.CITY, contact_data.get("city"))
        self.fill(self.STATE, contact_data.get("state"))
        self.fill(self.POSTAL, contact_data.get("postal"))
        self.fill(self.COUNTRY, contact_data.get("country"))

    def save_contact(self):
        # AI Healing is active here via BasePage click()
        self.click(self.SUBMIT_BTN)