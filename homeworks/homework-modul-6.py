from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/FabrykaTestowPW/chromedriver')
driver.get('https://fabrykatestow.pl/')

time.sleep(0.5)

kurs_taps_button = driver.find_element_by_xpath('//*[@id="menu-item-506"]/a')
kurs_taps_button.click()

element = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div/div/div/div/div/section[8]/div/div/div/div/div/div/div/h2')
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.5)

driver.save_screenshot("page_image.png")

driver.quit()
