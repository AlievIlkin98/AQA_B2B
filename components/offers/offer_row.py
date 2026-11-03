from playwright.sync_api import Locator, Page, expect

class OfferRow:
    def __init__(self, root: Locator):
        self.root = root

    """
    Локаторы
    """

    @property
    def add_to_cart_button(self) -> Locator:
        return self.root.get_by_test_id("exact-offer-add-to-cart")

    @property
    def increase_button(self) -> Locator:
        return self.root.get_by_test_id("product-qty-plus")

    @property
    def decrease_button(self) -> Locator:
        return self.root.get_by_test_id("product-qty-minus")

    @property
    def price(self) -> Locator:
        return self.root.get_by_test_id("exact-offer-price")

    @property
    def quantity_input(self) -> Locator:
        return self.root.get_by_test_id("product-qty-input")

    @property
    def delivery(self) -> Locator:
        return self.root.get_by_test_id("exact-offer-delivery")

    @property
    def returnable(self):
        return self.root.get_by_test_id("exact-offer-return")

    @property
    def stock(self):
        return self.root.get_by_test_id("exact-offer-stock")

    @property
    def lot(self):
        return self.root.get_by_test_id("exact-offer-lot")

    @property
    def availability(self) -> Locator:
        return self.root.get_by_test_id("exact-offer-availability")

    """
    Методы
    """
    def add_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def increase(self) -> None:
        self.increase_button.click()

    def decrease(self) -> None:
        self.decrease_button.click()



    """
       Значения атрибутов
    """

    def price_value(self) -> float:
        text = self.price.inner_text().replace(" ", "").replace(",", ".")
        return float(text)

    def delivery_value(self) -> str:
        return self.delivery.inner_text().strip()

