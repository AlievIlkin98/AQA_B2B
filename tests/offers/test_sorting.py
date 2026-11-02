from playwright.sync_api import expect
from pages.offers_page import OffersPage
import pytest

@pytest.mark.p1
def test_pr10_sort_by_cheapest(offers_page):
    """PR-10: Дешевле — цены по возрастанию внутри группы."""
    offers_page.sort_by_cheapest()
    groups = offers_page.prices_by_group()

    for name, prices in groups.items():
        assert prices == sorted(prices), f"{name}: {prices}"


@pytest.mark.p1
def test_pr11_sort_by_fastest(offers_page):
    """PR-11: Быстрее — первая доставка Сегодня или Завтра."""
    offers_page.sort_by_fastest()
    delivery = offers_page.offer(0).delivery_value()
    assert delivery in ("Сегодня", "Завтра"), delivery


def test_pr12_sort_by_recommended(offers_page):
    pass

def test_pr13_sort_persists_with_in_stock_filter(offers_page):
    pass




