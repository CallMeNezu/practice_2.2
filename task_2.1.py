import requests

urls= ['https://github.com/', 'https://www.binance.com/en',
       'https://tomtit.tomsk.ru/', 'https://jsonplaceholder.typicode.com/',
       'https://moodle.tomtit-tomsk.ru/']

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} доступен")
        else:
            print(f"{url} не доступен. Код: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"ошибка {url}: {e}")

