import requests
r = requests.get("http://qgc.qq.com/314962432/t/1")
print (type(r))
print (r.status_code)
print (r.encoding)
print (r.cookies)