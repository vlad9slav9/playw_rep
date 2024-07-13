import time

import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invalid_user', 'invalid_password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@pytest.mark.parametrize('username, password', [('user', 'user'), ('admin', 'admin')])
def test_login_success(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(f'Welcome {username}')
