from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import random
import requests

driver=webdriver.Chrome()
driver.get('https://divar.ir/s/iran/auto')
driver.maximize_window()
end_of_scroll=driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
    my_scroll=driver.execute_script('return document.body.scrollHeight')
    if my_scroll==end_of_scroll:
        break
    end_of_scroll=my_scroll


