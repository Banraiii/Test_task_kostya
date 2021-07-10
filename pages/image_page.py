from .base_page import BasePage
from .locators import MainPageLocators, ImagePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time 


class ImagePage(BasePage):
	def __init__(self, *args, **kwargs):
		super(ImagePage, self).__init__(*args, **kwargs)

	saving_deafult = None

	def shold_be_image_url(self, url):
		assert self.check_url(url),\
		"Нынешний url адрес не соотвествует введённому"

	def open_first_item_and_check_search_text(self):
		elem = self.driver.find_elements(*ImagePageLocators.ITEM_IMAGE_LINK_TEXT)[0]
		saving_first = self.save_element(*ImagePageLocators.ITEM_IMAGE_LINK_TEXT, elem)
		elem.click()
		assert self.shold_be_search_text_equel_text(*MainPageLocators.SEARCH_FIELD, saving_first.text),\
		"Поисковой запрос не соответсует категории"


	def open_first_image_check_is_present(self):
		self.is_element_present_and_visibl(*ImagePageLocators.COLLECTION_IMAGES)
		elem = self.driver.find_elements(*ImagePageLocators.COLLECTION_IMAGES)[0]
		elem.click()
		self.is_element_present_and_visibl(*ImagePageLocators.BIT_IMAGE)
		assert self.is_element_present(*ImagePageLocators.BIT_IMAGE),\
		'Картинка не открылась'
		element = self.driver.find_element(*ImagePageLocators.BIT_IMAGE)
		element_1 = element.get_attribute('src')
		return element_1

	def go_the_next_image(self, elem):
		right = self.driver.find_elements(*ImagePageLocators.CIRCLE_BUTTON_ICON)[3]
		right.click()
		assert self.element_no_equel_element(*ImagePageLocators.BIT_IMAGE, elem, 'src'),\
		"Картинки не изменились"

	def go_the_back_image(self, elem):
		left = self.driver.find_elements(*ImagePageLocators.CIRCLE_BUTTON_ICON)[0]
		left.click()
		assert self.element_equel_element(*ImagePageLocators.BIT_IMAGE, elem, 'src'),\
		"Картинки изменились"
