from playwright.sync_api import Page, Locator


class MarkupModel:
    def __init__(self, page: Page):
        self.page = page

    # TODO: заменить на data-testid по готовности
    # кнопка для открытия наценки
    @property
    def markup_button(self) -> Locator:
        # stub: get_by_test_id("markup-open")
        return self.page.get_by_text("Цена, ₽")

    #TODO: заменить на data-testid по готовности
    @property
    def root(self):
        return self.page.get_by_text('Настройка наценки')

    #TODO: заменить на data-testid по готовности
    @property
    def simple_tab(self):
        return self.root.get_by_title('Простая')

    # TODO: заменить на data-testid по готовности
    @property
    def complex_tab(self):
        return self.root.get_by_title('Сложная')

    # TODO: заменить на data-testid по готовности
    @property
    def apply_button(self) -> Locator:
        # stub: get_by_test_id("markup-apply")
        return self.root.get_by_role("button", name="Применить")

    # TODO: заменить на data-testid по готовности
    @property
    def reset_button(self) -> Locator:
        # stub: get_by_test_id("markup-reset")
        return self.root.get_by_role("button", name="Сбросить")


