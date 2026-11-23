from playwright.sync_api import Locator


class OfferRow:
    def __init__(self, root: Locator):
        self.root = root

        self.add_to_cart_button = root.get_by_test_id("exact-offer-add-to-cart")
        self.increase_button = root.get_by_test_id("product-qty-plus")
        self.decrease_button = root.get_by_test_id("product-qty-minus")
        self.quantity_input = root.get_by_test_id("product-qty-input")

        self.price = root.get_by_test_id("exact-offer-price")
        self.delivery = root.get_by_test_id("exact-offer-delivery")
        self.returnable = root.get_by_test_id("exact-offer-return")
        self.stock = root.get_by_test_id("exact-offer-stock")
        self.lot = root.get_by_test_id("exact-offer-lot")
        self.availability = root.get_by_test_id("exact-offer-availability")

    def add_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def increase(self) -> None:
        self.increase_button.click()

    def decrease(self) -> None:
        self.decrease_button.click()

    def price_value(self) -> float:
        text = self.price.inner_text().replace(" ", "").replace(",", ".")
        return float(text)

    def delivery_value(self) -> str:
        return self.delivery.inner_text().strip()

    def availability_value(self) -> str:
        return self.availability.inner_text().strip()