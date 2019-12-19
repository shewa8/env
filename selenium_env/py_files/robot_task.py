import math
import time
from selenium import webdriver


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element_by_css_selector('[type="text"]')
    input_answer.send_keys(y)

    check_box = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    check_box.click()

    radio_box = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio_box.click()

    sub_btn = browser.find_element_by_class_name('btn')
    sub_btn.click()

finally:
    time.sleep(10)
    browser.quit()
