import time
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="Resources/chromedriver.exe")
driver = webdriver.Chrome()
driver.get('https://www.calculator.net/bmi-calculator.html?ctype=metric')
driver.maximize_window()

age = driver.find_element(By.ID,'cage')
age.clear()
age.send_keys(20)
time.sleep(2)



gender = driver.find_element(By.CLASS_NAME,"cbcontainer")
driver.implicitly_wait(2)
ActionChains(driver).move_to_element(gender).click(gender).perform()
# male = driver.find_element(By.ID,'csex1')
# female = driver.find_element(By.ID,'csex2')
# ActionChains(driver).move_to_element(male).click(male).perform()
# ActionChains(driver).move_to_element(female).click(female).perform()


height = driver.find_element(By.ID,"cheightmeter")
height.clear()
height.send_keys(180)
time.sleep(2)


weight = driver.find_element(By.ID,"ckg")
weight.clear()
weight.send_keys(60)
time.sleep(2)


result = driver.find_element(By.XPATH,'//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/input[2]')
result.click()
time.sleep(2)

clr = driver.find_element(By.XPATH,'//*[@id="content"]/div[3]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/img')
clr.click()
time.sleep(2)

print('completed')

driver.close()



