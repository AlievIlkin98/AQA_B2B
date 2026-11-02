import pytest
from pages.offers_page import OffersPage

@pytest.fixture
def offers_page(logged_in_page, base_url):
    offers = OffersPage(logged_in_page, base_url)
    offers.open()
    offers.search("C1011")
    return offers

@pytest.fixture
def open_offers(logged_in_page, base_url):
    def _open(article: str = "C1011"):
        offers = OffersPage(logged_in_page, base_url)
        offers.open()
        offers.search(article)
        return offers
    return _open