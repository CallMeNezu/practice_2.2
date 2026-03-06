import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
if response.status_code != 200:
    print(f"ошибка: {response.status_code}")
    quit()

data = response.json()

def show_all_valute(data_def):
    currencies = data_def['Valute']
    for key, value in currencies.items():
        print(f"курс {value['Name']}({value['CharCode']}): {value['Value']} руб/ед.")

def show_valute_code(data_def):
    code_valute = input("введите сод валюты: ").strip().upper()
    if code_valute in data_def['Valute']:
        valute_info = data_def['Valute'][code_valute]
        print(f"текущий курс {valute_info['Name']}({code_valute}): {valute_info['Value']} руб./ед.")
    else:
        print(f"валюта по коду {code_valute} ненайдена")

def valute_groups():
    name_group = input("введите название группы: ")
    valute_group = input("введите названеи или код валюты: ").strip().upper()
    if name_group not in groups:
        groups[name_group] = []
    groups[name_group].append(valute_group)

def show_valute_groups():
    for name, group in groups.items():
        print(f"{name} : {group}")

def edition_groups(data_def):
    group_name = input("введите название группы: ")
    print(f"найдено! {group_name} : {groups[group_name]}")
    print('''выбирите:
    1 - добавить валюту
    2 - удалить валюту''')
    variant = input(":")
    if variant == "1":
        currencies = data_def['Valute']
        valute = input("введите код валюты которую хотите добавить: ").strip().upper()
        for key, value in currencies.items():
            if value['CharCode'] == valute:
                groups[group_name].append(valute)
                print("успешно добавленно!")
    if variant == "2":
        valute = input("введите код валюты которую хотите удалить: ").strip().upper()
        groups[group_name].remove(valute)
        print("успешно удалено!")

def save_groups_json(file_name):
    try:
        with open(file_name, "w") as file:
            json.dump(groups, file, indent=4)
        print("успешно сохронено в json файле!")
    except FileNotFoundError:
        print("файл ненайден.")

def read_save_groups(file_name):
    try:
        with open(file_name, "r") as f:
            groups_read = json.load(f)
        for group in groups_read:
            print(f"{group}: {groups_read[group]}")
            print(" ")
    except FileNotFoundError:
        print("файл ненайден.")

groups = {"основные валюты":['USD','EUR']}

while True:
    print("""введите:
    1 - посмотреть все валюты.
    2 - посмотреть валюту по коду.
    3 - создать группу валют и/или добавить туда валюту.
    4 - посмотреть все группы.
    5 - изменить список.
    6 - сохронить в json файле группы.
    7 - посмотреть группы из файла.
    0 - выйти""")
    answer = input(":")
    if answer == "1":
        show_all_valute(data)
    elif answer == "2":
        show_valute_code(data)
    elif answer == "3":
        valute_groups()
    elif answer == "4":
        show_valute_groups()
    elif answer == "5":
        edition_groups(data)
    elif answer == "6":
        save_groups_json("groups.json")
    elif answer == "7":
        read_save_groups("groups.json")
    elif answer == "0":
        quit()
    else:
        print("такого действия нет.")