from .basic_steps import BasicSteps
from selenium.webdriver.common.keys import Keys
import time


class MainPageSteps(BasicSteps):
    # нажатие на кнопки типа "Создать" или открытие найденной сущности
    def open_link_via_text_step(self, link_text):
        self.browser.find_element_by_partial_link_text("{}".format(link_text)).click()

    # метод переключения вкладок в блоке "Распределение обязанностей"
    def change_tab_step(self, tab):
        # self.browser.find_element_by_css_selector('#"{}"'.format(tab)).click()
        # self.browser.find_element_by_css_selector('body > div.wrap > section.requirements > section > div.graphs-errors.graph-active > a').click()
        self.browser.find_element_by_class_name("{}".format(tab)).find_element_by_tag_name("a").click()

    # метод получения текущей ссылки
    def get_current_url_step(self):
        current_link = self.browser.current_url
        return current_link

    # метод проверки ссылки
    def check_link_step(self, current_link, expected_link):
        assert current_link in expected_link
