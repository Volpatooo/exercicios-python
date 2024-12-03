from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def rpa_challenge_ocr():
    driver = webdriver.Chrome()
    driver.get('https://rpachallengeocr.azurewebsites.net/')
    time.sleep(2)
    button_start = driver.find_element(By.XPATH, "//*[@id='start']/button")
    button_start.click()
    time.sleep(3)


rpa_challenge_ocr()