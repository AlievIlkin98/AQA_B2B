from playwright.sync_api import Locator, Page, expect

class OfferRow:
    def __init__(self, root: Locator):
        self.root = root

    @property
    def add_to_cart_button(self) -> Locator:
        return self.root.get_by_test_id("exact-offer-add-to-cart")

    @property
    def increase_(self) -> Locator:
        return self.root.get_by_test_id("product-qty-plus")

    @property
    def decrease_button(self) -> Locator:
        return self.root.get_by_test_id("product-qty-minus")

    @property
    def price(self) -> Locator:
        return self.root.get_by_test_id('exact-offer-price')

    @property
    def delivery(self) -> Locator:
        return self.root.get_by_test_id('exact-offer-delivery')