from playwright.sync_api import expect
from pages.offers_page import OffersPage
import pytest

@pytest.mark.smoke
@pytest.mark.parametrize('detail_number', [("C1011")])
def test_add_offer_to_cart(logged_in_page, base_url, detail_number):
    offers = OffersPage(logged_in_page, base_url)
    offers.open()
    offers.search(detail_number)
    print(f'Предложений по {detail_number} : {offers.exact_offers.count()}' )

    offers.add_offer_to_cart()
    expect(offers.added_notice).to_be_visible()


def test_click_first_offer(logged_in_page, base_url):
    offers = OffersPage(logged_in_page, base_url)
    offers.open()
    offers.search("C1011")

    row = offers.exact_offers.first
    expect(row).to_be_visible()
    print("строка:", row.get_attribute("data-warehouse"))
    print('Доставка', row.get_by_test_id('exact-offer-delivery').inner_text())

    button = row.get_by_test_id("exact-offer-add-to-cart")
    expect(button).to_be_visible()
    button.click()

    expect(offers.added_notice).to_be_visible()
    print("тост:", offers.added_notice.inner_text())


#TODO: в разработке
def test_increase_offer_count(logged_in_page, base_url):
    offers = OffersPage(logged_in_page, base_url)
    offers.open()
    offers.search("C1011")

    row = offers.exact_offers.first
    expect(row).to_be_visible()

    row.get_by_test_id('exact-offer-add-to-cart').click()
    expect(offers.added_notice).to_be_visible()

    row.get_by_test_id('product-qty-plus').click()

    expect(row.get_by_test_id('product-qty-input')).to_be_visible()

