from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

use_step_matcher("re")


@given("User is on BMI calculator page")
def step_impl(context):
    # driver = webdriver.Chrome(executable_path="Resources/chromedriver.exe")
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.calculator.net/bmi-calculator.html?ctype=metric')
    context.driver.maximize_window()


@when("User clicks on Age 20")
def step_impl(context):
    age = context.driver.find_element(By.ID,'cage')
    age.clear()
    age.send_keys(20)
    time.sleep(2)


@step("User clicks on Gender Male")
def step_impl(context):
    gender = context.driver.find_element(By.CLASS_NAME, "cbcontainer")
    context.driver.implicitly_wait(2)
    ActionChains(context.driver).move_to_element(gender).click(gender).perform()


@step("User clicks on Height 180")
def step_impl(context):
    height = context.driver.find_element(By.ID, "cheightmeter")
    height.clear()
    height.send_keys(180)
    time.sleep(2)


@step("User clicks on Weight 60")
def step_impl(context):
    weight = context.driver.find_element(By.ID,"ckg")
    weight.clear()
    weight.send_keys(60)
    time.sleep(2)


@step("User clicks on Calculate button")
def step_impl(context):
    result = context.driver.find_element(By.XPATH,'//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/input[2]')
    result.click()
    time.sleep(2)


@then("User verify the result 18\.5")
def step_impl(context):
    clr = context.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/img')
    clr.click()
    time.sleep(2)