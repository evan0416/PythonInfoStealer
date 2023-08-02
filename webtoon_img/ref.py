import  os
import  requests

target_path = "C:\workspace\dark-web\webtoon_img"

image_url = 'https://image-comic.pstatic.net/webtoon/626907/237\
/20190115192015_d9f2b6e9d878a372dfa6f07ebfc5f14a_IMAG01_1.jpg'

# Referer을 지정하여 페이지를 통해서 요청
headers = {'Referer': 'https://comic.naver.com/webtoon/list.nhn?\
titleId=626907&weekday=wed'}

# response = requests.get(image_url, headers = headers)
response = requests.get(image_url, )
print(response) # 접속 확인 (200 = 성공)

image_data = response.content           # binary형식
img = os.path.basename(image_url)   # url을 이름으로 하는 비어있는 데이터생성

#파일에 이미지 데이터를 넣기
with open(img, 'wb') as f:
    f.write(image_data)