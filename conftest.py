import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="session")
def browser(playwright):
    # Укажите путь к исполняемому файлу Яндекс.Браузера
    #yandex_browser_path = "C:\\Users\\ASUS\\AppData\\Local\\Chromium\\Application\\chrome.exe"  # Замените на реальный путь

    browser = playwright.chromium.launch(headless=False) #(executable_path=yandex_browser_path, headless=False)

    yield browser
    browser.close()


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)