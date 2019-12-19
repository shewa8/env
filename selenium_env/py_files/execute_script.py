from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()