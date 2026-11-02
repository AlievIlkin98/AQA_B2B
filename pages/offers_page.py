from playwright.sync_api import Locator, Page, expect
from  components.offers.markup_model import MarkupModel
from components.offers.offer_row import OfferRow


class OffersPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.markup = MarkupModel(page)


    @property
    def search_input(self) -> Locator:
        return self.page.get_by_test_id("header-search-input")

    @property
    def in_stock_checkbox(self) -> Locator:
        return self.page.get_by_test_id("price-filter-in-stock")

    @property
    def exact_offers(self) -> Locator:
        return self.page.get_by_test_id("exact-offer-row")

    @property
    def added_notice(self) -> Locator:
        return self.page.get_by_text("добавлена в корзину")

    @property
    def copied_notice(self) -> Locator:
        return self.page.get_by_text("Артикул скопирован")

    #Data-test-id расположен в 2-х местах, фронту необходимо исправить
    @property
    def markup_button(self) -> Locator:
        return self.page.get_by_test_id("price-settings-button")

    @property
    def search_clear_button(self) -> Locator:
        return self.page.get_by_test_id("header-search-clear")

    @property
    def copy_button(self):
        return self.page.get_by_test_id("exact-product-copy-sku")

    @property
    def cheaper_sort_tub(self):
        return self.page.get_by_test_id("price-sort-cheaper")

    @property
    def faster_sort_tub(self):
        return self.page.get_by_test_id("price-sort-faster")

    def open(self) -> None:
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        expect(self.search_input).to_be_visible()

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_input.press("Enter")
        expect(self.exact_offers.first).to_be_visible()

    def offer(self, index: int = 0) -> OfferRow:
        return OfferRow(self.exact_offers.nth(index))

    def open_markup(self) -> MarkupModel:
        self.markup_button.click()
        expect(self.markup.root).to_be_visible()
        return self.markup

    def search_clear(self) -> None:
        self.search_clear_button.click()

    def copy(self) -> None:
        self.copy_button.click()

    def sort_by_cheapest(self) -> None:
        self.cheaper_sort_tub.click()

    # Сортировка по табу "Быстрее"
    def sort_by_fastest(self) -> None:
        self.faster_sort_tub.click()

    # Сбор цен по группам
    def prices_by_group(self) -> dict[str, list[float]]:
        groups: dict[str, list[float]] = {}
        for i in range(self.exact_offers.count()):
            row = self.offer(i)
            group = row.availability_value()
            groups.setdefault(group, []).append(row.price_value())
        return groups

    def filter_by_stock(self) -> None:
        self.in_stock_checkbox.click()

    def filter_by_faster(self) -> None:
        self.in_stock_checkbox.click()







