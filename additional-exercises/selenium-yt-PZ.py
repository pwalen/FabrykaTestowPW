from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def wait(driver_instance, idk, time_to_wait=10):
    try:
        elem = WebDriverWait(driver, time_to_wait).until(EC.visibility_of_element_located((By.ID, idk)))
    except TimeoutException:
        elem = False
    return elem


driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/FabrykaTestowPW/chromedriver')

driver.get('https://youtube.com')

no_thanks = driver.find_element_by_id('dismiss-button')

wait(driver, 'dismiss-button')

no_thanks.click()

wait(driver, 'iframe')

iframe = driver.find_element_by_id('iframe')

driver.switch_to.frame(iframe)

wait(driver, 'introAgreeButton')

driver.find_element_by_id('introAgreeButton').click()

driver.quit()
