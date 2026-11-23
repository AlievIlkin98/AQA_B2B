from playwright.sync_api import Locator, Page, expect


class FilterModal:
    def __init__(self, page: Page):
        self.page = page

        self.root = page.get_by_test_id("filter-modal")  # окно фильтров
        self.apply_button = self.root.get_by_test_id("filter-modal-apply")
        self.clear_button = self.root.get_by_role("button", name="Очистить все")
        self.close_button = self.root.get_by_test_id("filter-modal-close")

        self.brand_items = self.root.get_by_test_id("filter-brand-item")  # строки брендов
        self.brand_search = self.root.get_by_placeholder("Поиск по названию")

        self.delivery_section = self.root.get_by_test_id("filter-delivery")  # блок срока доставки
        self.return_section = self.root.get_by_test_id("filter-warranty")  # блок срока возврата
        self.price_section = self.root.get_by_test_id("filter-price")  # блок цены

        self.price_from = self.root.get_by_placeholder("от")
        self.price_to = self.root.get_by_placeholder("до")

    def should_be_open(self) -> None:
        """Окно фильтров открыто."""
        expect(self.root).to_be_visible()

    def select_brand(self, index: int = 0) -> None:
        """Выбрать бренд по номеру в списке."""
        self.brand_items.nth(index).click()

    def search_brand(self, name: str) -> None:
        """Найти бренд по названию в поле поиска."""
        self.brand_search.fill(name)

    def price(self, name: str) -> None:
        """Выбрать готовый вариант цены: «до 1000», «1000 и дороже», «Неважно»."""
        self.price_section.get_by_text(name, exact=True).click()

    def price_range(self, from_value: str, to_value: str) -> None:
        """Задать свой диапазон цены от–до."""
        self.price_from.fill(from_value)
        self.price_to.fill(to_value)

    def delivery(self, name: str) -> None:
        """Выбрать срок доставки."""
        self.delivery_section.get_by_text(name, exact=True).click()

    def returns(self, name: str) -> None:
        """Выбрать срок возврата."""
        self.return_section.get_by_text(name, exact=True).click()

    def apply(self) -> None:
        """Применить фильтры и закрыть окно."""
        self.apply_button.click()

    def clear(self) -> None:
        """Сбросить все выбранные фильтры."""
        self.clear_button.click()

    def close(self) -> None:
        """Закрыть окно без применения."""
        self.close_button.click()