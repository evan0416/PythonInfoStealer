import requests

headers = {
    "User-Agent" : "Android",
    # "Referer" : "https://www.nate.com"
}


res = requests.get("http://www.nate.com",
                        verify= False, headers= headers,
                          allow_redirects=False)


# print(type(res.status_code))            #type check

# headers ={
#     "User-Agent" : "Android",
#     "Referer" : "https://www.nate.com"
# }

# if "Location" in res.headers or res.status_code == 302:
#     res2 = requests.get(res.headers["Location"],
#                         verify=False,
#                         headers=headers)
    

fd = open("c.html", "wb")
fd.write(res.content)
fd.close()
print(res.content)