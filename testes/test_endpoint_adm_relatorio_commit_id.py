#!/usr/bin/env python3
from globals import targetHost

def testGet():
    import requests
    url_base = targetHost
    post_login = requests.post(f'{url_base}/login', data = {'login': 'admin', 'apiKey': '328c7358201991879ae9aaedbedd4af2d4f723eb1a52d788f541537bf2828c4a'})
    print('Login feito')
    token = post_login.json()['access_token']
    headers = {
    'Authorization': f'Bearer {token}'
    }
    response = requests.get(url_base+'/adm_relatorio/1', headers=headers)
    print(response)
    print(response.text)
    return 0
    
def testDelete():
    import requests
    url_base = targetHost
    post_login = requests.post(f'{url_base}/login', data = {'login': 'admin', 'apiKey': '328c7358201991879ae9aaedbedd4af2d4f723eb1a52d788f541537bf2828c4a'})
    print('Login feito')
    token = post_login.json()['access_token']
    headers = {
    'Authorization': f'Bearer {token}'
    }
    response = requests.delete(url_base+'/adm_relatorio/1', headers=headers)
    print(response)
    print(response.text)
    return 0

try:
    print('rodando teste Get')
    testGet()
    print('rodando teste Delete')
    testDelete()
    print('----------------------------------------------------------------------------------------------------------------------')
except Exception as e:
    print(e)
