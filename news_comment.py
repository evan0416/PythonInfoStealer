import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

browser = webdriver.Chrome()

browser.get("https://n.news.naver.com/mnews/article/comment/001/0014006478?sid=100")
browser.implicitly_wait(5)
time.sleep(random.randint(3,5))
for c_box in browser.find_elements(By.CLASS_NAMEm "u_e"):
    contents = c_box.find_element(By.CLASS_NAME)
input()