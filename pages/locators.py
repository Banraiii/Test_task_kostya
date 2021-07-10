from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	SEARCH_FIELD = (By.CSS_SELECTOR,".search2__input .input__box .input__control")
	SUGGEST_TABEL = (By.CSS_SELECTOR,".mini-suggest__popup-content")
	IMAGE_LINK_IMAGE = (By.LINK_TEXT, "Картинки")

class ResultPageLocators():
	RESULT_LINKS = (By.CSS_SELECTOR,".content__left .serp-item")
	LINK_IN_SUBTITLE = (By.CSS_SELECTOR,'.serp-item .organic .organic__subtitle b')

class ImagePageLocators():
	RESULT_LINKS = (By.CSS_SELECTOR,".content__left .serp-item")
	ITEM_IMAGE_LINK_TEXT = (By.CSS_SELECTOR,'.PopularRequestList .PopularRequestList-SearchText')
	COLLECTION_IMAGES = (By.CSS_SELECTOR,'.serp-list .serp-item')
	BIT_IMAGE = (By.CSS_SELECTOR,'.MMImageContainer .MMImage-Preview')
	CIRCLE_BUTTON_ICON = (By.CSS_SELECTOR,'.CircleButton .CircleButton-Icon')