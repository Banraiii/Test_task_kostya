from .base_page import BasePage
from .locators import ResultPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

class ResultPage(BasePage):
	def __init__(self, *args, **kwargs):
		super(ResultPage, self).__init__(*args, **kwargs)

	def should_be_five_result_link(self,num0,num1,num2,num3,num4):
		time.sleep(1)
		self.should_be_in_first_link_word_tensor(num0)
		self.should_be_in_two_link_word_tensor(num1)
		self.should_be_in_three_link_word_tensor(num2)
		self.should_be_in_four_link_word_tensor(num3)
		self.should_be_in_five_link_word_tensor(num4)

	def should_be_in_first_link_word_tensor(self, number):
		assert self.word_equel_tensor(number), f"Error message!( { number } ссылка не соответсвует tensor.ru)"

	def should_be_in_two_link_word_tensor(self, number):
		assert self.word_equel_tensor(number), f"Error message!( { number } ссылка не соответсвует tensor.ru)"

	def should_be_in_three_link_word_tensor(self, number):
		assert self.word_equel_tensor(number), f"Error message!( { number } ссылка не соответсвует tensor.ru)"


	def should_be_in_four_link_word_tensor(self, number):
		assert self.word_equel_tensor(number), f"Error message!( { number } ссылка не соответсвует tensor.ru)"

	def should_be_in_five_link_word_tensor(self, number):
		assert self.word_equel_tensor(number), f"Error message!( { number } ссылка не соответсвует tensor.ru)"
