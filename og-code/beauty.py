from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

browser = webdriver.Chrome()
num = 1
while True:
	print(num)
	url = "https://comic.naver.com/webtoon/detail?titleId=648419&no="+ str(num) +"&weekday=mon"
	browser.get(url)	
	time.sleep(5)
 
	os.mkdir(str(num-1))
	if url != browser.current_url:
		break
	browser.find_element(By.CLASS_NAME,'view')
	title = browser.find_element(By.CLASS_NAME,'view').find_element(By.TAG_NAME, 'h3').text.replace("<","[").replace(">","]")
	if "화" not in title:
		title = str(num) + "화_" + title
	wt_viewer = browser.find_element(By.CLASS_NAME, 'wt_viewer')
	index = 1
	headers = {'Referer': url, 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
	for img in wt_viewer.find_elements(By.TAG_NAME, "img"):
		img_src = img.get_attribute('src')
		response = requests.get(img_src, headers= headers)

		if index < 10:
			filename = title + "_00" + str(index) + ".jpg"
		elif index < 100:
			filename = title + "_0" + str(index) + ".jpg"
		else:
			filename = title + "_" + str(index) + ".jpg"	
		#print filename.replace("<","[").replace(">","]")
		fd = open(".\\" + str(num-1) + "\\" + filename, "wb")
		fd.write(response.content)
		fd.close()
		response.close()
		index += 1
	num += 1
browser.close()

