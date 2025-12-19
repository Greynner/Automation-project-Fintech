from playwright.sync_api import Page, expect
from config import (
    PAYPAL_BASE_URL,
    PAYPAL_LOGIN_URL,
    PAYPAL_LOGIN_LINK_TEXT,
    PAYPAL_EMAIL_SELECTOR,
    PAYPAL_NEXT_SELECTOR,
    PAYPAL_PASSWORD_SELECTOR,
    PAYPAL_SUBMIT_SELECTOR,
    PAYPAL_OTP_TITLE_TEXT,
)

class SendMoneyPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto(PAYPAL_BASE_URL, wait_until="domcontentloaded")

    # ---------------------------
    # QUICKLINK / ENTRY POINT
    # ---------------------------
    @property
    def send_money_quicklink(self):
        # Screenshot: role link name "Send money"
        return self.page.get_by_role("link", name="Send money")

    # ---------------------------
    # RECIPIENT STEP
    # ---------------------------
    @property
    def recipient_input(self):
        # Screenshot: role combobox, name "Name, username, email, mobile"
        return self.page.get_by_role("combobox", name="Name, username, email, mobile")

    @property
    def recipient_suggestions(self):
        # Suggestions list items are role="option"
        return self.page.get_by_role("option")

    def recipient_option_for(self, email: str):
        # Screenshot: option name "Send to: sb-xxxx@personal.example.com"
        return self.page.get_by_role("option", name=f"Send to: {email}")

    # ---------------------------
    # AMOUNT / CURRENCY / NOTE
    # ---------------------------
    @property
    def amount_input(self):
        # Screenshot: aria-label="Enter amount field" role textbox
        return self.page.get_by_role("textbox", name="Enter amount field").or_(
            self.page.locator("#fn-amount")
        )

    @property
    def currency_selector(self):
        # Screenshot: role combobox, aria-label="Select currency"
        return self.page.get_by_role("combobox", name="Select currency").or_(
            self.page.get_by_test_id("currency-selector-button")
        )

    @property
    def note_textarea(self):
        # Screenshot: textbox name "What's this for?" id="noteField"
        return self.page.get_by_role("textbox", name="What's this for?").or_(
            self.page.locator("#noteField")
        )

    @property
    def details_next_button(self):
        # Screenshot: big button "Next" (after amount/note)
        return self.page.get_by_role("button", name="Next")

    @property
    def cancel_link(self):
        return self.page.get_by_role("link", name="Cancel")

    @property
    def back_link(self):
        return self.page.get_by_role("link", name="Back")

    # ---------------------------
    # PAYMENT METHOD CHOICE
    # ---------------------------
    @property
    def paypal_balance_choice(self):
        # Screenshot: text "PayPal Balance (USD)"
        return self.page.get_by_text("PayPal Balance", exact=False)

    @property
    def visa_choice(self):
        # Screenshot: text "Visa"
        return self.page.get_by_text("Visa", exact=False)

    @property
    def payment_choice_next_button(self):
        # Screenshot: data-testid="choice-next-button" text Next
        return self.page.get_by_test_id("choice-next-button").or_(
            self.page.get_by_role("button", name="Next")
        )

    # ---------------------------
    # REVIEW / SEND
    # ---------------------------
    @property
    def send_button(self):
        # Screenshot: button text "Send"
        return self.page.get_by_role("button", name="Send")

    # ---------------------------
    # ACTIONS (high level)
    # ---------------------------
    def open_send_money(self):
        self.send_money_quicklink.click()

    def select_recipient(self, recipient_email: str):
        expect(self.recipient_input).to_be_visible()
        self.recipient_input.click()
        self.recipient_input.fill(recipient_email)

        # Wait and click the specific option if it appears
        option = self.recipient_option_for(recipient_email)
        expect(option).to_be_visible()
        option.click()

    def enter_amount(self, amount: str):
        expect(self.amount_input).to_be_visible()
        self.amount_input.click()
        # PayPal a veces deja "0.00" seleccionado; fill lo reemplaza bien.
        self.amount_input.fill(amount)

    def enter_note(self, note: str):
        expect(self.note_textarea).to_be_visible()
        self.note_textarea.click()
        self.note_textarea.fill(note)

    def go_next_from_details(self):
        expect(self.details_next_button).to_be_enabled()
        self.details_next_button.click()

    def choose_payment_method_balance_and_next(self):
        # Selecciona PayPal Balance (si ya está seleccionado igual no pasa nada)
        expect(self.paypal_balance_choice).to_be_visible()
        self.paypal_balance_choice.click()
        expect(self.payment_choice_next_button).to_be_enabled()
        self.payment_choice_next_button.click()

    def review_and_send(self):
        expect(self.send_button).to_be_enabled()
        self.send_button.click()

    # ---------------------------
    # FULL FLOW (convenience)
    # ---------------------------
    def send_money(self, recipient_email: str, amount: str, note: str = "Test"):
        self.open_send_money()
        self.select_recipient(recipient_email)
        self.enter_amount(amount)
        if note:
            self.enter_note(note)
        self.go_next_from_details()
        self.choose_payment_method_balance_and_next()
        self.review_and_send()
