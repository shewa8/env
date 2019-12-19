from selenium import webdriver
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys('Vladyslav')
    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys('Shevchenko')
    mail = browser.find_element_by_css_selector('[name="email"]')
    mail.send_keys('shewa8@gmail.com')

    file = browser.find_element_by_css_selector('[name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_input.txt')
    file.send_keys(file_path)

    btn = browser.find_element_by_class_name("btn")
    btn.click()


finally:
    time.sleep(5)
    browser.quit()