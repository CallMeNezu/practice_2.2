import requests

def show_profile(username_1):
    try:
        url = f'https://api.github.com/users/{username_1}'
        response = requests.get(url)
        if response.status_code == 200:
            user_data = response.json()
            print("имя:", user_data['name'])
            print("ссылка на профиль: ", user_data['html_url'])
            print("количество репозиториев: ", user_data['public_repos'])
            print("количество подписчиков: ", user_data['followers'])
            print("количество подписок: ", user_data['following'])
        else:
            print("Ошибка:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("ошибка при получении данных")

def show_all_repositories(username_2):
    try:
        repos_url = f'https://api.github.com/users/{username_2}/repos'
        headers_task_2 = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(repos_url, headers=headers_task_2)
        repositories = response.json()
        if response.status_code == 200:
            for repo in repositories:
                print(" ")
                print("название: ", repo["name"])
                print("ссылка: ",repo["html_url"])
                print("язык прогромирования: ",repo["language"])
                if repo["private"]:
                    print("статус: приватный")
                else:
                    print("статус: публичный")
                print("ветка по умолчанию: ",repo["default_branch"])

                # Получаем статистику просмотра отдельно
                views_url = f'{repo["url"]}/traffic/views'
                traffic_response = requests.get(views_url, headers=headers_task_2)
                print("просмотров: ",traffic_response.json().get('count'))
    except requests.exceptions.RequestException as e:
        print("ошибка при получении данных")

def show_repositories(username_3, repos_name):
    try:
        url = f'https://api.github.com/users/{username_3}/repos'
        headers_task_3 = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(url, headers=headers_task_3)
        repos = response.json()
        if response.status_code == 200:
            for repo in repos:
                if repo['name'] == repos_name:
                    print(" ")
                    print("название: ", repo["name"])
                    print("ссылка: ", repo["html_url"])
                    print("язык прогромирования: ", repo["language"])
                    if repo["private"]:
                        print("статус: приватный")
                    else:
                        print("статус: публичный")
                    print("ветка по умолчанию: ", repo["default_branch"])

                    views_url = f'{repo["url"]}/traffic/views'
                    traffic_response = requests.get(views_url, headers=headers_task_3)
                    print("просмотров: ", traffic_response.json().get('count'))
    except requests.exceptions.RequestException as e:
        print("ошибка при получении данных")

username = input("введите свой username: ")
while True:
    print("""введите:
    1 - посмотреть информацию о профиле
    2 - посмотреть все репозитории
    3 - посмотреть конкретный репозиторий
    4 - сменить username
    0 - выйти""")
    variant = input(":")
    if variant == "1":
        show_profile(username)
    elif variant == "2":
        show_all_repositories(username)
    elif variant == "3":
        repositories_name = input("введите название репозитория: ")
        show_repositories(username, repositories_name)
    elif variant == "4":
        username = input("введите новый username: ")
    elif variant == "0":
        quit()
    else:
        print("такого действия нет.")