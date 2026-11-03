import pytest
from playwright.sync_api import expect


@pytest.mark.p1
def test_pr20_filter_in_stock_only(offers_page):
    """PR-20: фильтр в наличии оставляет только строки В наличии."""
    offers_page.filter_by_stock()

    for i in range(offers_page.exact_offers.count()):
        row = offers_page.offer(i)
        expect(row.availability).to_have_text("В наличии")


@pytest.mark.p1
def test_pr21_filter_returnable_only(offers_page):
    """PR-21: только возвратные, без Невозврат."""
    offers_page.filter_by_returnable()

    for i in range(offers_page.exact_offers.count()):
        row = offers_page.offer(i)
        expect(row.returnable).not_to_have_text("Невозврат")

#TODO: выполнить после создани компонента analog
@pytest.mark.p1
def test_pr22_reset_quick_filters(offers_page):
    """PR-22: Сброс фильтров."""
    pass

@pytest.mark.p1
def test_pr23_switch_part_type_tabs(offers_page):
    """PR-23: Переключение табов с типами деталей."""
    pass

#TODO: необходим data-testid на табы
@pytest.mark.p2
def test_pr24_all_tab_counter_equals_sum(offers_page):
    """PR-24: Счётчик «Все» равен сумме типов."""
    pass

#TODO: необходим data-testid на табы
def test_pr25_zero_count_tab_is_disabled(offers_page):
    """PR-24: Счётчик «Все» равен сумме типов."""

