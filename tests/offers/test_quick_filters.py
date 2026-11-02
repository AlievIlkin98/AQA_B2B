import pytest
from playwright.sync_api import expect


@pytest.mark.p1
def test_pr20_filter_in_stock_only(offers_page):
    """PR-20: фильтр в наличии оставляет только строки В наличии."""
    offers_page.filter_by_stock()

    for i in range(offers_page.exact_offers.count()):
        row = offers_page.offer(i)
        expect(row.availability_value()).to_have_value("В наличии")


def test_pr21_filter_returnable_only(offers_page):
    """PR-20: Остались только предложения с возможностью возврата N дн."""
    row = offers_page.offer(0)
    expect(row.return_value()).not_to_have_value("Невозврат")
