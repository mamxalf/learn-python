import requests

req = requests.get('https://google.com')
status = req.status_code
print(status)
