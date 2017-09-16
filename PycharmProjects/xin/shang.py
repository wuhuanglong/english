

import requests
def get_all_cookie():
    r = requests.get("http://qgc.qq.com/314962432")
    c = r.cookies
    i = c.items()
    for name, value in i :
        print (name, value)
def get_all_cookie2():
    session = requests.Session()
    response = session.get("http://qgc.qq.com/314962432")
    print (session.cookies.get_dict())
if  __name__  == "__main__":
    get_all_cookie2()