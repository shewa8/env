from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, ("input"))
    for element in elements:
        element.send_keys("Hello")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
