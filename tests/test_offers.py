from playwright.sync_api import expect
from pages.offers_page import OffersPage


def test_add_c1011_to_cart(logged_in_page, base_url):
    page = logged_in_page
    page.goto(base_url, wait_until="domcontentloaded")

    search = page.get_by_test_id("header-search-input")
    search.fill("C1011")
    search.press("Enter")

    offers = page.get_by_test_id("exact-offer-row")
    expect(offers.first).to_be_visible()
    print(f"предложений по C1011: {offers.count()}")

    first = offers.first
    warehouse = first.get_attribute("data-warehouse")
    price = first.get_by_test_id("exact-offer-price").inner_text()
    delivery = first.get_by_test_id("exact-offer-delivery").inner_text()
    print(f"первый оффер: {warehouse}, цена {price}, доставка {delivery}")

    first.get_by_test_id("exact-offer-add-to-cart").click()

    notice = page.get_by_text("добавлена в корзину")
    expect(notice).to_be_visible()
    print(f"уведомление: {notice.inner_text()}")

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

