import time
import pytest
from get_data import dataReader
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

'''
get data from excel file in list[tuple(email address, expectation result),]
'''
data = dataReader.readDataForLogin()

@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=options)
    # driver.minimize_window()
    driver.get('http://gmail.com')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.mark.parametrize('emailAddress, expected', data)
def test_googleAccount(driver, emailAddress, expected):
    emailField = driver.find_element_by_id('identifierId')
    emailField.send_keys(emailAddress)
    nextButton = driver.find_element_by_id('identifierNext')
    nextButton.click()
    time.sleep(3)

    text = driver.find_element_by_id('headingText').text
    assert text == expected


    # try:
    #     WebDriverWait(driver,10).until(EC.text_to_be_present_in_element())
    #     text = driver.find_element_by_id('headingText').text
    #     assert text == 'Selamat datang'
    
    # except TimeoutException:
    #     pass
