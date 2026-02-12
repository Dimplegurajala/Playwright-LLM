from .base_page import BasePage

class LoginPage(BasePage):
    def navigate(self):
        self.page.goto("https://thinking-tester-contact-list.herokuapp.com/")

    def login(self, email, password):
        self.fill("#email", email)
        self.fill("#password", password)
        self.click("#submit")