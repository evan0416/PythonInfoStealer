# import requests

# headers={
   
# }

# url=""

# data={

# }


# response =requests.get(url,headers=headers,data=data)



#  "Cookie": "NNB=QTMDGNJHTMZWI; nid_inf=-1288902096; NID_AUT=n4xNkN8VaTTNWEWZ/sSrryWF2eur9MpFN4A1YQkoWtr4vOIro7qcjSabbakWJpno; NID_JKL=gow1Jfl1l89Iw//avhZNRgMAu4jB+M9ZVJHR5Qv3Yn0=; SHP_BUCKET_ID=3; nx_ssl=2; page_uid=i4pGLdprvTossF/1Rhwssssss64-259519; spage_uid=i4pGLdprvTossF%2F1Rhwssssss64-259519; NID_SES=AAABsWQQOfcxatTPIW/0Qa2b0RMUJbI40ogg95Fom1U42zP4vg/wWKBFpRDDWUEFaK1kiUvteJrgqnNkvGwNlOkfHTJKJ8a1X4g029YsXqJAGNXreLhSrgsB9o1pwMTa9yIo+LPoywArnbSEXlKOXMxbUfcFFoZ02oZhSPy87u1snSmWOAFV0hvqsd7dBKs8nl1CAB94on/HTE9PR0PK2v3UAhrlgv3cdjICLruOAWre4JoCuIga4MAwY8V3Dd5apnhKCws/ZcXYITXXy7xZh6OMBGhczWw3vjVaIbivsqMOtsNVPCXX2vTUTorIbE9+jPBMi1zmW7VFv+xcG1CB5SbgpOVV+6gJexGlZbnDpDnMBNwReOTXNGR1asKbGXfE6fhOSg3QaIueDRpiXGWHETAfVVVDeHWSBKAAw0BDwYRHB
import requests

headers={
    "Host":"search.shopping.naver.com",
    "Content-Type":"application/json",
    "Cookie":"NNB=QTMDGNJHTMZWI; nid_inf=-1288902096; NID_AUT=n4xNkN8VaTTNWEWZ/sSrryWF2eur9MpFN4A1YQkoWtr4vOIro7qcjSabbakWJpno; NID_JKL=gow1Jfl1l89Iw//avhZNRgMAu4jB+M9ZVJHR5Qv3Yn0=; SHP_BUCKET_ID=3; nx_ssl=2; page_uid=i4qP8sprvTossgjlQcNssssssB8-479090; NID_SES=AAABtF62wZa/NcbXjzKjzCLKAEmVENIv6AAcyYlgfgjyEall/Z5JqW05gYEiMB/zbT/fGI684Z8IIyYDMTlD/+dHrm/ey8Orn3E4XQ//q2xVY+o5LFHVoySYOyVsIfRsH26+ZlcpO0jTrP6bfKE8wyrlrDZPCoTBxUxCRNvnJTHrf7w2mUC97R7vIenvDrTw8oFZjecwfD18sryJ9kbk60uAx9K0HmeZGCnZgofTS7xlCBrlTxFZGIJWFdaC0v4NzoeePriLi3r97YeoIDc+oanjsT4zRxsjMSW1tCzRUbJGj85JpnHs+VWX4vHC8sIdkMV6lyvhtAKJVcQY64FbkFbBeVqJVweuBww4kp2uoB2cB8Hmg4hetKobVuoE1Bc0K3ME0MjVQj+In3qxHiTn+irQacsFyYnD6X7UyOvnPcy3Pi2mVF7/ON8cNKx2opvMwj790SGcOHreSKdCUE5M61Tk33u5pXZMS48jtyB2DDQk1JJNWM3nHpEykPtulC7CcIJeDxhst4l1t9+JVoauzWpnuqRNmGONRT9UBi24EOrUI35HgBAt3MNlzcOdXFjbmWeKZaiqlZMQsrK57Ok4q9RHqL4=; spage_uid=i4qP8sprvTossgjlQcNssssssB8-479090; sus_val=3zBqq+XVxVq9QBGXzeNVZfOi; ncpa=95694|liwp13a0|440eb11d77cc369c4853daf8705d6a18d002a248|95694|0ebe4fa914f322f435bb612dc24aa4036f486cdd",
    "Referer":"https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=%EC%82%BC%EA%B2%B9%EC%82%B4",
    "Sbth":"0e067b473eba76cf1fc405a4baaf65939b1b8e4b0b2abd09c0c0349a55cd46292ef71dc78b8d3f43eeacfab441fad2ec",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


data={
    "chpid": "",
    "isAd": False,
    "isAdult":False,
    "isBook": False,
    "isHotdeal": False,
    "nvMid":str(81967078701),
    "tr":"slsl"
}
response=requests.post("https://search.shopping.naver.com/api/product-zzim/add",headers=headers,json=data)
print(response.content)