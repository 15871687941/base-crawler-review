import requests
from lxml import etree
from fake_useragent import UserAgent

# 1、构造会话对象
session = requests.session()

# 2、添加请求头
ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

session.headers = headers

# 2、请求首页
response = session.get(url="https://accounts.douban.com/passport/login?source=main")

print(response.text, session.cookies)