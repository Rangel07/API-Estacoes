#!/usr/bin/env python3
from globals import targetHost
def testPost():
    import requests
    url_base = targetHost
    post = requests.post(f'{url_base}/login', data = {'login': 'admin', 'apiKey': '328c7358201991879ae9aaedbedd4af2d4f723eb1a52d788f541537bf2828c4a'})
    print(post)
    return 0

try:
    print('rodando teste Post')
    testPost()
    print('-------------------------------------------------------------------------------------------------------------------------------')
except Exception as e:
    print(e)
