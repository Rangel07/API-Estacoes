#!/usr/bin/env python3
from globals import targetHost
def testPost():
    import requests
    url_base = targetHost
    post = requests.post(f'{url_base}/cadastro', data = {'login': 'teste_', 'email': 'emailImaginario@nuvens'})
    print(post)
    print(post.text)
    return 0

try:
    print('rodando teste Post')
    testPost()
    print('-------------------------------------------------------------------------------------------------------------------------------')
except Exception as e:
    print(e)
