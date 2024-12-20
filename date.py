from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get('https://demoqa.com/date-picker')
driver.maximize_window()

sleep(1)
date_input = driver.find_element(By.XPATH, '//*[@id="dateAndTimePickerInput"]')
date_input.clear()
date_input.send_keys('12/30/2024')
driver.find_element(By.XPATH,'//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[2]').click()
start_date = datetime.datetime.today()
end_date = start_date + datetime.timedelta(days=10)
print(end_date)
file.close()