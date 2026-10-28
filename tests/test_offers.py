from playwright.sync_api import expect
from pages.offers_page import OffersPage
import pytest


@pytest.fixture
def offers_page(logged_in_page, base_url):
    offers = OffersPage(logged_in_page, base_url)
    offers.open()
    offers.search("C1011")
    return offers

def test_add_offer(offers_page):
    row = offers_page.offer(0)
    row.add_to_cart()
    expect(offers_page.added_notice).to_be_visible()


#TODO: в разработке
def test_increase_offer_count(offers_page):
    row = offers_page.offer(0)
    row.add_to_cart()
    expect(row.increase_button).to_be_visible()
    row.increase()
    expect(row.quantity_input).to_have_value(2)

def test_decrease_offer_count(offers_page):
    row = offers_page.offer(0)
    row.add_to_cart()
    expect(row.decrease_button).to_be_visible()
    row.increase()
    expect(row.quantity_input).to_have_value(2)
    row.decrease()
    expect(row.quantity_input).to_be_equal(1)
