from playwright.sync_api import Locator, Page, expect

class CardPage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    @property
    def cart_icon(self) -> Locator:
        return self.page.get_by_test_id("header-cart-count")

    #TODO: вернуть data-testid как будет готово
    @property
    def checkout_button(self) -> Locator:
        return self.page.get_by_role("button", name="Перейти к оформлению")

    def open(self) -> None:
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        self.cart_icon.click()
        expect(self.checkout_button).to_be_visible()