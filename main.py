import requests

url = 'https://detik.com'
try:
    req = requests.get(url)
    print('OK !', req.status_code)
except Exception as e:
    print('Notice : ', e)
