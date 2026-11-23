from playwright.sync_api import Locator, Page, expect

from components.offers.filter_modal import FilterModal
from components.offers.markup_model import MarkupModel
from components.offers.offer_row import OfferRow


class OffersPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.markup = MarkupModel(page)
        self.filters = FilterModal(page)

        self.search_input = page.get_by_test_id("header-search-input")  # поле поиска
        self.search_clear_button = page.get_by_test_id("header-search-clear")  # крестик очистки поиска
        self.copy_button = page.get_by_test_id("exact-product-copy-sku")  # копировать артикул

        self.in_stock_checkbox = page.get_by_test_id("price-filter-in-stock")  # чекбокс «в наличии»
        self.returnable_checkbox = page.get_by_test_id("price-filter-returnable")  # чекбокс «только возвратные»
        self.filter_open_button = page.get_by_test_id("price-filter-open")  # открыть модалку фильтров

        self.exact_offers = page.get_by_test_id("exact-offer-row")  # строки искомого артикула
        self.added_notice = page.get_by_text("добавлена в корзину")  # тост добавления в корзину
        self.copied_notice = page.get_by_text("Артикул скопирован")  # тост копирования

        self.markup_button = page.get_by_test_id("price-settings-button")  # открыть наценку
        self.cheaper_sort_tab = page.get_by_test_id("price-sort-cheaper")  # сортировка «Дешевле»
        self.faster_sort_tab = page.get_by_test_id("price-sort-faster")  # сортировка «Быстрее»

    def open(self) -> None:
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        expect(self.search_input).to_be_visible()

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_input.press("Enter")
        expect(self.exact_offers.first).to_be_visible()

    def offer(self, index: int = 0) -> OfferRow:
        return OfferRow(self.exact_offers.nth(index))

    def open_filters(self) -> FilterModal:
        self.filter_open_button.click()
        expect(self.filters.root).to_be_visible()
        return self.filters

    def open_markup(self) -> MarkupModel:
        self.markup_button.click()
        expect(self.markup.root).to_be_visible()
        return self.markup

    def search_clear(self) -> None:
        self.search_clear_button.click()

    def copy(self) -> None:
        self.copy_button.click()

    def sort_by_cheapest(self) -> None:
        self.cheaper_sort_tab.click()
        expect(self.exact_offers.first).to_be_visible()

    def sort_by_fastest(self) -> None:
        self.faster_sort_tab.click()
        expect(self.exact_offers.first).to_be_visible()

    def prices_by_group(self) -> dict[str, list[float]]:
        groups: dict[str, list[float]] = {}
        for i in range(self.exact_offers.count()):
            row = self.offer(i)
            group = row.availability_value()
            groups.setdefault(group, []).append(row.price_value())
        return groups

    def filter_by_stock(self) -> None:
        self.in_stock_checkbox.click()

    def filter_by_returnable(self) -> None:
        self.returnable_checkbox.click()
