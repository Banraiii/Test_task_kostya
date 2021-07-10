from .base_page import BasePage
from .locators import MainPageLocators, ResultPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time 

class MainPage(BasePage):
	def __init__(self, *args, **kwargs):
		super(MainPage, self).__init__(*args, **kwargs)

	def should_be_search_field(self):
		assert self.is_element_present(*MainPageLocators.SEARCH_FIELD),\
		"Должно быть поле поиска"

	def enter_words_in_search_field(self, words):
		search = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
		search.click()
		search.send_keys(str(words))

	def should_be_hint_table(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.SUGGEST_TABEL),\
		'должно присутствовать в DOM и видемо на страничке'

	def after_press_Enter_appears_result_tabl(self):
		elem = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
		elem.send_keys(Keys.RETURN)
		assert self.is_element_present_and_visibl(*ResultPageLocators.RESULT_LINKS),\
		'Отсутсвует список результатов поиска'

	def should_be_image_link_on_yandex_image(self):
		assert self.is_element_present(*MainPageLocators.IMAGE_LINK_IMAGE),\
		"Должна быть ссылка-картинка на картинки яндекс"

	def go_to_the_yandex_images_from_image_link(self):
		self.click_on_button(*MainPageLocators.IMAGE_LINK_IMAGE)
		new_window = self.driver.window_handles[1]
		self.driver.switch_to.window(new_window)