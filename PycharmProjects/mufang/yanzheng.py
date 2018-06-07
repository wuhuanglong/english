import requests
from requests.exceptions import RequestException
import re
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return  response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    patten = re.compile('<p><.*?title="(.*?)"/></p>.*?<a.*?title="(.*?)">(.*?)</a>.*?(.*?)</dd>',re.S)
    items = re.findall(patten,html)
    print(items)
def main():
    url = "http://qgc.qq.com/314962432"
    html = get_one_page(url)
    parse_one_page(html)
if __name__ == "__main__":
    main()
