
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import random
import requests
import divar_url

url=divar_url.shiraz_url
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
end_of_scroll=driver.execute_script('return document.body.scrollHeight')

for i in range(0,5):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(5)
    my_scroll=driver.execute_script('return document.body.scrollHeight')
    if my_scroll==end_of_scroll:
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/main/div/div[1]/div/button').click()
        time.sleep(1)
    end_of_scroll=my_scroll
text=driver.find_elements(By.CLASS_NAME,'kt-post-card__body')
for t in text:
    print(t.text)
print("end")
    






