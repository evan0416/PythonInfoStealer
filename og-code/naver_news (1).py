import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
import openpyxl
browser = webdriver.Chrome()
book= openpyxl.Workbook()
sheet = book.active
browser.get("https://n.news.naver.com/mnews/article/comment/001/0014006478?sid=100")
browser.implicitly_wait(5)
time.sleep(random.randint(3,5))
while True:
    try:
        u_cbox_btn_more = browser.find_element(By.CLASS_NAME, "u_cbox_btn_more")
        u_cbox_btn_more.click()
        time.sleep(2)
    except:
        break
for c_box in browser.find_elements(By.CLASS_NAME, "u_cbox_area"):
    
    try:
        contents = c_box.find_element(By.CLASS_NAME, "u_cbox_contents")
        print(contents.text)
        sheet.append([contents.text])
    except:
        pass
    
book.save("result.xlsx")

book.close()
input()
browser.close()