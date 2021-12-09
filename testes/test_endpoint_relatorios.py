#!/usr/bin/env python3
from globals import targetHost
def testGet():
    import requests
    url_base = targetHost
    post_login = requests.post(f'{url_base}/login', data = {'login': 'estacao_teste', 'apiKey': '489a845537412def5431c0b0022bac0022dd00dadcb971bf375c862e5b1f0085'})
    print('Login feito')
    token = post_login.json()['access_token']
    headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
    }
    response = requests.get(url_base+'/relatorios', headers=headers)
    print(response)
    
    return 0
def testPost():
    import requests
    import json
    url_base = targetHost
    post_login = requests.post(f'{url_base}/login', data = {'login': 'estacao_teste', 'apiKey': '489a845537412def5431c0b0022bac0022dd00dadcb971bf375c862e5b1f0085'})
    print('Login feito')
    token = post_login.json()['access_token']

    payload = json.dumps({
    "lista": [{
        "dataHora": "2021-10-01 17:18:00",
        "id_estacao": 3,
        "pontoOrvalho": 120,
        "pressaoAtmosferica": 200,
        "direcaoVento": 5,
        "radiacaoSolar": 3.5,
        "temperaturaAr" : 25,
        "velocidadeVento" : 2.6,
        "pluviometro" : 1.1,
        "umidade" : 65.1
        }]
    })
    headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
    }
    response = requests.post(url_base+'/relatorios', headers=headers, data=payload)
    print(response)
    print(response.text)
    return 0
try:
    print('rodando teste Get')
    testGet()
    print('rodando teste Post')
    testPost()
    print('----------------------------------------------------------------------------------------------------------------------')
except Exception as e:
    print(e)
