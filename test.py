
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Abdul Moeed\\Downloads\\chromedriver_win32\\chromedriver.exe")

url = 'https://demoqa.com/'

driver.get(url)


driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]').click()
time.sleep(2)


driver.find_element_by_xpath('//*[@id="item-0"]').click()
time.sleep(2)


driver.find_element_by_xpath('//*[@id="userName"]').send_keys('Abdul Moeed')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('22-11043@formanite.fccollege.edu.pk')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="currentAddress"]').send_keys('Lahore Cantt')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="permanentAddress"]').send_keys('Same as above')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(2)

driver.quit()
