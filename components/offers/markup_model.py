from playwright.sync_api import Locator, Page, expect


class MarkupModel:
    def __init__(self, page: Page):
        self.page = page

    @property
    def root(self) -> Locator:
        # stub: get_by_test_id("markup-modal")
        return self.page.get_by_test_id("markup-settings-modal")

    @property
    def simple_tab(self) -> Locator:
        return self.root.get_by_test_id("markup-type-simple")

    @property
    def complex_tab(self) -> Locator:
        return self.root.get_by_test_id("markup-type-complex")

    @property
    def percent_radio(self) -> Locator:
        return self.root.get_by_role("radio", name="Процент")

    @property
    def sum_radio(self) -> Locator:
        return self.root.get_by_role("radio", name="Сумма")

    @property
    def simple_value_input(self) -> Locator:
        return self.root.get_by_test_id("markup-value-input")

    @property
    def apply_button(self) -> Locator:
        return self.root.get_by_test_id("markup-apply-button")

    @property
    def reset_button(self) -> Locator:
        return self.root.get_by_test_id("markup-reset-button")

    @property
    def close_button(self) -> Locator:
        return self.root.get_by_test_id("markup-modal-close")

    def should_be_open(self) -> None:
        expect(self.root).to_be_visible()

    def open_simple(self) -> None:
        self.simple_tab.click()

    def open_complex(self) -> None:
        self.complex_tab.click()

    def set_percent(self, value: str) -> None:
        self.percent_radio.click()
        self.simple_value_input.fill(value)

    def set_sum(self, value: str) -> None:
        self.sum_radio.click()
        self.simple_value_input.fill(value)

    def apply(self) -> None:
        self.apply_button.click()

    def reset(self) -> None:
        self.reset_button.click()

    def close(self) -> None:
        self.close_button.click()