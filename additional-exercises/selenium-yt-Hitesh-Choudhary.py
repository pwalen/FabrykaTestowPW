# Web automation in python for beginners
# url: https://youtu.be/f7LEWxX4AVI
# "the plan is really simple I want to open up the web site youtube.com
# and I want to pass on a simple query on that so there is a search box at the top
# and I really want to type my name and hit this button but through the script"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/FabrykaTestowPW/chromedriver')
driver.get('https://www.youtube.com/')

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                            '/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/div[2]'))).click()

# time.sleep(5)
# driver.switch_to_alert().accept()

# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH,
#                                 '/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/div[2]'))).click()

# no_thanks_button = driver.find_element_by_xpath('//*[@id="button"]')
# no_thanks_button.click()

# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('Hitesh Choudhary')
#
# search_button = driver.find_element_by_xpath('//*[@id="search-button"]')
# search_button.click()
