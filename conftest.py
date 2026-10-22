import os

import pytest
from playwright.sync_api import Browser, Page, expect

# адрес стенда
BASE_URL = "https://rim-dev.ixora-auto.ru"

# тестовый пользователь
LOGIN = "LIZA"
PASSWORD = "654321"

# сюда сохранится "я уже залогинен" — cookies и localStorage
STATE_PATH = os.path.join(os.path.dirname(__file__), ".auth", "user.json")

# без широкого окна сайт включает мобильную вёрстку и ломает расценку
VIEWPORT = {"width": 1920, "height": 1080}


# адрес сайта, чтобы не писать его в каждом тесте
@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


# scope="session" — логин один раз на весь pytest, не перед каждым тестом
@pytest.fixture(scope="session")
def auth_state(browser: Browser, base_url: str) -> str:
    # создать папку .auth, если её нет
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)

    # чистый браузер, ещё без cookies
    context = browser.new_context(viewport=VIEWPORT)
    page = context.new_page()

    # открыть форму. domcontentloaded — не ждать метрику и карты
    page.goto(f"{base_url}/auth", wait_until="domcontentloaded")

    # клик в поле нужен, иначе Ant Design не включает кнопку «Войти»
    page.locator("#login_login").click()
    page.locator("#login_login").fill(LOGIN)
    page.locator("#login_password").click()
    page.locator("#login_password").fill(PASSWORD)
    page.locator("#login_password").press("Tab")

    # кнопка disabled, пока форма не увидит ввод
    submit = page.get_by_role("button", name="Войти")
    expect(submit).to_be_enabled(timeout=10000)
    submit.click()

    # дождаться ухода с /auth — значит пустили внутрь
    page.wait_for_url(lambda url: "/auth" not in url)

    # сохранить cookies в файл и закрыть этот браузер
    context.storage_state(path=STATE_PATH)
    context.close()

    # наружу отдаём только путь к файлу
    return STATE_PATH


# новый браузер уже с cookies из файла
# свой контекст на каждый тест, чтобы тесты не мешали друг другу
@pytest.fixture
def logged_in_context(browser: Browser, auth_state: str):
    context = browser.new_context(storage_state=auth_state, viewport=VIEWPORT)
    yield context
    context.close()


# вкладка внутри залогиненного браузера
# именно её получает тест как аргумент logged_in_page
@pytest.fixture
def logged_in_page(logged_in_context) -> Page:
    page = logged_in_context.new_page()
    yield page
    page.close()