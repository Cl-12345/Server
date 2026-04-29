import requests, time

url = 'https://desmos666.online'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
}
while True:
    k = requests.get(url, headers=headers)
    print(k.status_code)
    k.close()
    time.sleep(1.5)
