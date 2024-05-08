#copy this and paste into the terminal
# pip install requests
# pip install win10toast

import requests
from win10toast import ToastNotifier
import json
import time

def update():
    url = "https://api.covid19india.org/data.json"
    response = requests.get(url)
    data = response.json()
    cases = data['statewise'][0]['confirmed']
    deaths = data['statewise'][0]['deaths']
    recovered = data['statewise'][0]['recovered']
    active = data['statewise'][0]['active']
    print("Total Cases: ", cases)
    print("Total Deaths: ", deaths)
    print("Total Recovered: ", recovered)
    print("Total Active: ", active)

    message = "Total Cases: " + str(cases) + "\nTotal Deaths: " + str(deaths) + "\nTotal Recovered: " + str(recovered) + "\nTotal Active: " + str(active)

    toaster = ToastNotifier()
    toaster.show_toast("Covid-19 Update", message, duration=10)

while True:
    update()
    time.sleep(3600)


