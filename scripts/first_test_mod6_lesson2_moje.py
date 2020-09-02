from selenium import webdriver

import time

for i in range(10):
    driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/FabrykaTestowPW/chromedriver')

    driver.get('https://google.pl')

    search_box = driver.find_element_by_name('q')

    search_box.send_keys('selenium python')

    search_box.submit()

    driver.quit()
