# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import random
# import time

# browser = webdriver.Chrome()
# browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
# # browser.get("https://www.naver.com/")
# browser.implicitly_wait(5)
# time.sleep(random.randint(3,5))

# # id_ =browser.find_element(By.ID, By.NAME, By.TAG_NAME)

# #when fine link 
# # for  a in browser.find_elements(By.TAG_NAME, "a"):
# #     try: print(a.get_attribute("href"))
# #     except:pass


# id_ = browser.find_element(By.NAME, "id")
# # id_.click()
# id_.send_keys("naver_id")
# pw =browser.find_element(By.ID, "pw")
# # pw.click()
# pw.send_keys("naver_pw")


# login_button =browser.find_element(By.XPATH, '//*[@id="log.login"]')
# input()
# browser.close()




# ���덈땲�� �밸뱶�쇱씠踰� 紐⑤뱢
from selenium import webdriver
# ���덈땲�� �밸뱶�쇱씠踰꾩뿉�� WebElement 瑜� 李얘린�꾪븳 媛앹껜 By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# �ъ씠�� 濡쒕뵫 �� �쒕뜡�쒓컙 湲곕떎由ш린 �꾪븳 �쒕뜡 �⑥닔
import random, time, pyperclip
# 釉뚮씪�곗� 媛앹껜 �몄텧
browser = webdriver.Chrome()
# 釉뚮씪�곗�瑜� 二쇱냼李쎌쓣 �듯빐 濡쒓렇�� �섏씠吏� �묎렐
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
# 釉뚮씪�곗� 臾듭떆�� ��湲�
browser.implicitly_wait(5)
# �쒕뜡�쒓컙 ��湲�
time.sleep(random.randint(3, 5))
# �� �섏씠吏��먯꽌 id, pw �낅젰李� 李얘퀬 kisia 媛� �낅젰 �� �쒕뜡�쒓컙 ��湲�
id_ = browser.find_element(By.NAME, "id")
#id_.send_keys("kisia_test")
pyperclip.copy("kisia_test")
id_.send_keys(Keys.CONTROL, 'v')
time.sleep(random.randint(1, 2))
pw = browser.find_element(By.ID, "pw")
#pw.send_keys("kisia_test1234")
pyperclip.copy("kisia_test1234")
pw.send_keys(Keys.CONTROL, 'v')
time.sleep(random.randint(1, 2))
# 濡쒓렇�� 踰꾪듉�� xpath濡� 李얘퀬 �대┃
login_button = browser.find_element(By.XPATH, '//*[@id="log.login"]')
login_button.click()


input()
browser.close()