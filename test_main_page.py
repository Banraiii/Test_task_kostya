from .pages.main_page import MainPage
from .pages.result_page import ResultPage
from .pages.image_page import ImagePage
import pytest
import time

@pytest.mark.all_test
class TestLoginFromMainPage():	
	@pytest.mark.search_in_yandex
	def test_search_in_yandex(self, driver):
		link = 'https://yandex.ru/'
		yandex_page = MainPage(driver, link)
		yandex_page.open()
		yandex_page.should_be_search_field()
		yandex_page.enter_words_in_search_field('Тензор')
		yandex_page.should_be_hint_table()
		yandex_page.after_press_Enter_appears_result_tabl()
		result_page = ResultPage(driver, driver.current_url)
		result_page.should_be_five_result_link(0,1,2,3,4)

	@pytest.mark.yandex_images
	def test_yandex_images(self,driver):
		link = 'https://yandex.ru/'
		yandex_page = MainPage(driver, link)
		yandex_page.open()
		yandex_page.should_be_image_link_on_yandex_image()
		yandex_page.go_to_the_yandex_images_from_image_link()
		image_page = ImagePage(driver, driver.current_url)
		image_page.shold_be_image_url('https://yandex.ru/images/') #Преход с домашней ст. яндекса 09.07.2021, ведёт на https://yandex.ru/images/?utm_source=main_stripe_big так, что сделал вхождение 
		image_page.open_first_item_and_check_search_text()
		save_element_6_like_src_value = image_page.open_first_image_check_is_present()
		image_page.go_the_next_image(save_element_6_like_src_value)
		image_page.go_the_back_image(save_element_6_like_src_value)
		#time.sleep(3)
