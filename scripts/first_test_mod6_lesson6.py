from selenium import webdriver

import time

driver = webdriver.Chrome('/Users/pawelwalenda/PycharmProjects/FabrykaTestowPW/chromedriver')

url = 'https://google.pl'

driver.get(url)

search_box = driver.find_element_by_name('q')

search_box.send_keys('selenium python')

search_box.submit()

time.sleep(5)

driver.quit()

driver.close()
# <input type='text' name='password_input' id='some_id'/>

element = driver.find_element_by_name('password_input')
element1 = driver.find_element_by_id('some_id')
element2 = driver.find_element_by_xpath('//input[@id="some_id]')
