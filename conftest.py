import pytest

@pytest.fixture(scope="session")
def browser(playwright):
    # Укажите путь к исполняемому файлу Яндекс.Браузера
    yandex_browser_path = "C:\\Users\\KSK-SHOP\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"  # Замените на реальный путь

    browser = playwright.chromium.launch(executable_path=yandex_browser_path, headless=False)

    yield browser
    browser.close()
