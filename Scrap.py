
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import divar_url
import Sql


url = divar_url.iran_url
num_scroll =200


driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
end_of_scroll = driver.execute_script('return document.body.scrollHeight')

cars_list = []


for i in range(0, num_scroll):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(5)
    my_scroll = driver.execute_script('return document.body.scrollHeight')
    if my_scroll == end_of_scroll:
        time.sleep(3)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/main/div/div[1]/div/button').click()
        time.sleep(1)
    end_of_scroll = my_scroll
    text = driver.find_elements(By.CLASS_NAME, 'kt-post-card__body')
    for t in text:
        text = str(t.text)
        cars_list.append(text.split('\n'))

    post_tilte = driver.find_elements(By.CLASS_NAME, 'kt-post-card__title')
    post_description = driver.find_elements(
        By.CLASS_NAME, 'kt-post-card__description')

driver.close()
#insert data to sql
print(len(cars_list))
Sql.insert_to_database(cars_list)



