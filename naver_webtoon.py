from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os
import random

num =1
browser = webdriver.Chrome()    #browser obj call

while True:
    url = "https://comic.naver.com/webtoon/list?titleId=796152&ng=" +str(num)
    browser.get(url)
    browser.implicitly_wait(5)
    time.sleep(random.randint(3,5))

    title = browser.find_element(By.ID, " titleName_toolbar")
    ep  = browser.find_element(By.ID, "subtitle_toolbar")
    print
    



browser.implicitly_wait(5)
time.sleep(5)

