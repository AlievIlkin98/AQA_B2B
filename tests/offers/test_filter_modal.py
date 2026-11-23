import pytest
from playwright.sync_api import Page, expect



#TODO: доработать кейс
@pytest.mark.p1
def test_pr30_open_filters_modal_default_values(offers_page, filters_modal):
    """PR-30: Нажать кнопку Фильтровать.
       Ожидаемый результат: открыта расценка, предложения отображены на странице
       """
    filters_modal.should_be_open()

@pytest.mark.p1
def test_pr31_close_filters_without_apply(offers_page, filters_modal):
    """PR-31: Закрыть окно фильтрации.
           Ожидаемый результат: окно закрыто
           """
    expect(filters_modal.root).to_be_visible()
    filters_modal.close()
    expect(filters_modal.root).not_to_be_visible()

@pytest.mark.p1
def test_pr32_filter_price_up_to_1000(offers_page, filters_modal):
    """PR-32: цена до 1000 — в выдаче нет дороже."""
    filters_modal.price_range("0","1000")
    filters_modal.apply()

    expect(offers_page.exact_offers.first).to_be_visible()
    for i in range(offers_page.exact_offers.count()):
        assert offers_page.offer(i).price_value() <= 1000


@pytest.mark.p1
def test_pr33_filter_price_from_1000(offers_page, filters_modal):
    """PR-33: цена от 1000."""
    filters_modal.price_range("1000", "")
    filters_modal.apply()

    expect(offers_page.exact_offers.first).to_be_visible()
    for i in range(offers_page.exact_offers.count()):
        price = offers_page.offer(i).price_value()
        assert 1000 <= price <= 2000, price

@pytest.mark.p1
def test_pr34_filter_price_range(offers_page, filters_modal):
    """PR-34: цена от 500 до 1000."""
    filters_modal.price_range("500", "1000")
    filters_modal.apply()
    expect(offers_page.exact_offers.first).to_be_visible()
    for i in range(offers_page.exact_offers.count()):
        price = offers_page.offer(i).price_value()
        assert 500 <= price <= 1000, f"цена {price} вне диапазона 500–1000"

def test_pr36_filter_delivery_time(offers_page, filters_modal):

    pass