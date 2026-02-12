
import pytest
import time
from pages.login_page import LoginPage
from pages.contact_list_page import ContactListPage
from pages.add_contact_page import AddContactPage

@pytest.mark.must_have
@pytest.mark.parametrize("contact_data", [
    {
        "first": "Dimple",
        "last": "SDET",
        "dob": "1995-01-01",
        "email": "dimple.qa@celcom.com",
        "phone": "8005551234",
        "street1": "123 Main St",
        "street2": "Apt 4B",
        "city": "Bangalore",
        "state": "Karnataka",
        "postal": "560001",
        "country": "India"
    }
])
def test_e2e_add_contact_full_form(page, healer, logger, contact_data):
    #prevent duplicate 
    timestamp = int(time.time())
    unique_email = f"dimple.{timestamp}@celcom.com"
    contact_data["email"] = unique_email
    # 1. Login
    login = LoginPage(page, healer, logger)
    login.navigate()
    login.login("testuserdimple@example.com", "Password123")
    
    # 2. Navigate to Form
    dashboard = ContactListPage(page, healer, logger)
    dashboard.navigate_to_add_contact()
    
    # 3. Fill and Submit Full Form
    form = AddContactPage(page, healer, logger)
    form.fill_contact_details(contact_data)
    form.save_contact()
    
    page.wait_for_load_state("networkidle")
    # 4. Data Integrity Verification
    dashboard.verify_contact_present(contact_data["email"])