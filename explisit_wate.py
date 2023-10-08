from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
try:
	print("Browser Start!")
	driver.get("https://poltava.ortosano.com.ua")		# открываем страницу

	massage=WebDriverWait(driver, 13).until(				# ждем 13 сек пока появиться строка по CSS -->
	# EC.element_to_be_clickable((By.XPATH, "//div[@class = 'alert alert-success']"))
	EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=tp-linesplit]"))
	)
	# на 10 секундах и меньше тест не проходит
finally:
	driver.quit()
	print("Browser quit!")


