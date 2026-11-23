import pytest
from pages.offers_page import OffersPage

@pytest.fixture
def offers_page(logged_in_page, base_url):
    """Открытая страница расценки детали С1011."""
    offers = OffersPage(logged_in_page, base_url)
    offers.open()
    offers.search("C1011")
    return offers

@pytest.fixture
def open_offers(logged_in_page, base_url):
    """Открытая страница расценки детали по любой детали."""
    def _open(article: str = "C1011"):
        offers = OffersPage(logged_in_page, base_url)
        offers.open()
        offers.search(article)
        return offers
    return _open

@pytest.fixture
def filters_modal(offers_page):
    """Открытая модалка фильтров на расценке по C1011."""
    return offers_page.open_filters()