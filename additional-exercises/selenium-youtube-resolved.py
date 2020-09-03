# How to circumvent two popups when opening 'www.youtube.com' with Selenium Webdriver?

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/FabrykaTestowPW/chromedriver')
driver.get('https://www.youtube.com/')

# ! We will close the “Sign in to YouTube” popup, by clicking the “NO, THANKS” button:
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button'))).click()

# ! We will switch to the second popup - “Before you continue” 🍪
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//*[@id="iframe"]')))

# ! We will close it by clicking the “I AGREE” button.
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME,
                                                            '#introAgreeButton'))).click()
