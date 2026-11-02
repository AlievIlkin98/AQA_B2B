from playwright.sync_api import expect
from pages.offers_page import OffersPage
import pytest


@pytest.mark.p0
def test_pr01_search_by_article_opens_pricing(offers_page):
    """PR-01: Ввести артикул в строку поиска, нажать Enter.
    Ожидаемый результат: открыта расценка, предложения отображены на странице
    """
    expect(offers_page.exact_offers.first).to_be_visible()
    expect(offers_page.search_input).to_have_value("C1011")
    expect(offers_page.exact_offers.first).to_be_visible()


@pytest.mark.p0
def test_pr02_pricing_table_has_required_columns(offers_page):
    """PR-02: Ввести артикул в строку поиска, нажать Enter.
    Ожидаемый результат: открыта расценка, предложения отображены на странице
    """
    row = offers_page.offer(0)
    expect(row.price).to_be_visible()
    expect(row.add_to_cart_button).to_be_visible()
    expect(row.price).to_be_visible()
    expect(row.delivery).to_be_visible()
    expect(row.returnable).to_be_visible()
    expect(row.stock).not_to_be_visible()


#TODO: уточнить у аналитика предмет проверки
@pytest.mark.p1
def test_pr03_offer_row_has_all_fields(offers_page):
    pass


@pytest.mark.p1
def test_pr04_search_nonexistent_article_shows_empty_state(open_offers):
    """PR-04: Ввести несуществующий артикул в строку поиска, нажать Enter.
        Ожидаемый результат: пользователю отображена страница с сообщением 'Проверьте, пожалуйста, правильно ли указан номер детали, VIN или номер кузова.'
        """
    offers = open_offers("asdqwef")
    expect(offers.exact_offers).to_have_count(0)



@pytest.mark.p1
def test_pr05_clear_search_input_by_cross(offers_page):
    """PR-05: очистка поле поиска.
            Ожидаемый результат: пользователю отображена страница с сообщением
            """
    offers_page.search_clear()
    expect(offers_page.search_input).to_have_value("")


@pytest.mark.p2
def test_pr06_change_brand_updates_pricing(offers_page):
    """PR-06: очистка поле поиска.
                Ожидаемый результат: пользователю отображена страница с сообщением
                """
    pass


@pytest.mark.p2
def test_pr07_copy_article_to_clipboard(offers_page):
    """PR-07: копирование артикула показывает уведомление"""
    offers_page.copy()
    expect(offers_page.copied_notice).to_be_visible()