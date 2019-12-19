from selenium import webdriver

try:
    link = "https://stepik.org/lesson/228249/step/2?unit=200781"
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    browser.quit()