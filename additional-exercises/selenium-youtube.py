from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/FabrykaTestowPW/chromedriver')
driver.get('https://www.youtube.com/')

# ! zamykamy pierwsze wyskakujące okienko “Sign in to YouTube”, klikając na “NO, THANKS”.
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button'))).click()

# ! zamykamy drugie wyskakujące okienko “Before you continue”, klikając na “I AGREE”. 🍪
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/div[2]'))).click()

# the “I AGREE” button:
# full xpath: '/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/div[2]'
# xpath: '//*[@id="introAgreeButton"]/div[2]'

# the “I AGREE” text (on the button):
# full xpath: '/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span'
# xpath: '//*[@id="introAgreeButton"]/span/span'
