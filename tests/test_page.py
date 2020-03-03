import pytest
import time
from steps.main_page_steps import MainPageSteps
from constants.constants import *


def test_check_monosnap_link(browser, link=MAIN_PAGE, tab=ERRORS_TAB, link_text=MONOSNAP_LINK_TEXT, expected_link=MONOSNAP_LINK):
    # открываем браузер
    main_page = MainPageSteps(browser, url=link)
    main_page.open_browser_step()
    # открываем вкладку "Находить несовершенства"
    main_page.change_tab_step(tab=tab)
    # открываем ссылку "Софт для быстрого создания скриншотов"
    main_page.open_link_via_text_step(link_text=link_text)
    # получаем ссылку открывшейся страницы
    current_link = main_page.get_current_url_step()
    # провверяем открывшуюся ссылку
    main_page.check_link_step(current_link=current_link, expected_link=expected_link)
