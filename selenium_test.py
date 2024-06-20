from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = webdriver.ChromeOptions()
# отключает режим показа браузера
# options.add_argument('--headless')
# пример других опций, которые вы можете использовать
# options.add_argument('--disable-gpu')
# options.add_argument("--disable-popup-blocking")
# создать драйвер браузера Chromium
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# получить страницу
driver.get("http://127.0.0.1:8000")
print(driver.title)
sleep(10)
driver.close()
