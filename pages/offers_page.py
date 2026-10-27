from playwright.sync_api import Locator, Page, expect
from  components.offers.markup_model import MarkupModel
from components.offers.offer_row import OfferRow


class OffersPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.markup = MarkupModel(page)


    # поле поиска в шапке
    @property
    def search_input(self) -> Locator:
        return self.page.get_by_test_id("header-search-input")

    # Строка предложения
    @property
    def exact_offers(self) -> Locator:
        return self.page.get_by_test_id("exact-offer-row")

    # тост «добавлена в корзину»
    @property
    def added_notice(self) -> Locator:
        return self.page.get_by_text("добавлена в корзину")

    def open(self) -> None:
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        expect(self.search_input).to_be_visible()

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_input.press("Enter")
        expect(self.exact_offers.first).to_be_visible()

    # Кнопка добавления в корзину
    def add_offer_to_cart(self) -> None:
        self.exact_offers.first.get_by_test_id("exact-offer-add-to-cart").click()
        expect(self.added_notice).to_be_visible()


    #TODO: после доработки MarkupModel исправить
    def open_markup(self) -> MarkupModel:
        # stub: get_by_test_id("markup-open")
        self.markup.markup_button.click()
        expect(self.markup.root).to_be_visible()
        return self.markup

    # Атрибут получения цены первого оффера
    def get_offer_price(self):
        return self.exact_offers.first.get_by_test_id("exact-offer-price")

    def get_offer_stock(self):
        return self.exact_offers.first.get_by_test_id("exact-offer-stock")

    # Раскрытие списка аналогов "Показать еще"
    def exact_product_show_all(self):
        self.page.get_by_test_id("exact-product-show-all").inner_text()

    def check_exact_product_show_all_is_visible(self):
        expect(self.exact_product_show_all).to_be_visible()


    def first_offer(self) -> OfferRow:
        return OfferRow(self.exact_offers.first)




