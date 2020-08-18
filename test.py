from selenium import webdriver

import unittest

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('hola')
driver.find_element_by_name('submit_search').click()
#print(driver.find_element_by_xpath('//*[@id="center_column"]/p/font/font').text)
#time.sleep(5)
#tc.assertEqual('No se encontraron resultados para tu búsqueda "hola"', driver.find_element_by_xpath('//*[@id="center_column"]/p/font/font').text )

driver.close()
driver.quit()
