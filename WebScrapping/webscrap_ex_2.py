#! python3

import requests

#open url using request.get() method - it will return response object
link = "https://automatetheboringstuff.com/files/rj.txt"
req = requests.get(link)
# use this instance object to check the request status

req_status = req.status_code
print("Request status: ",req_status) # 404 error is not found, 200 is okay.
#print("Content : ",req.text)
print("Content length : ",len(req.text))

#easier way to check the request status is by using request.raise_for_status()
#code : 
#bad_req  = requests.get("https://automatetheboringstuff.com/files/asdasdasdsa.txt")
#bad_req.raise_for_status()

f = open("RomeoandJuliet.txt","wb") # always write binary when use request module
for chunk in req.iter_content(5000):
    f.write(chunk)
f.close()
