from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# говоримо    шукати кожен елемент на протязі 5 секунд
driver.implicitly_wait(2)
driver.maximize_window()
try:
	print("Browser Start!")
	driver.get("https://casenik.com.ua/user/login")	# открываем страницу

	inpUt_email = driver.find_element(By.XPATH, "//input[@id = 'email']")
	inpUt_email.send_keys("igor2@gmail.com")
	password_ = driver.find_element(By.XPATH, "//input[@id = 'pasword']")
	password_.send_keys("qwer432!")
	login_button = driver.find_element(By.XPATH, '//button[@class = "btn button-gen"]').click()

	massage = WebDriverWait(driver, 28).until_not(
		# EC.element_to_be_clickable((By.XPATH, "//div[@class = 'alert alert-success']"))
		EC.visibility_of_element_located((By.XPATH, "//div[@class = 'alert alert-success']"))
	)	# ждем 30 сек пока не исчезнет строка по Х пасу

	time.sleep(5)
finally:
	driver.quit()
	print("Browser quit!")


