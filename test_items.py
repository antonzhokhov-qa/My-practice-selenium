
import time
# from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button"), "No basket button"
