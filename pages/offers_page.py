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
    def exact_offers(self) -> Locator:
        return self.page.get_by_test_id("exact-offer-row")

    @property
    def added_notice(self) -> Locator:
        return self.page.get_by_text("добавлена в корзину")

    #Data-test-id расположен в 2-х местах, фронту необходимо исправить
    @property
    def markup_button(self) -> Locator:
        return self.page.get_by_test_id("price-settings-button")

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






