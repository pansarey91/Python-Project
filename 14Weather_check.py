# pip install bs4
import requests
from bs4 import BeautifulSoup

print("\n Hello welcome to weather checker\n ")

search = input("Enter city name: ")
url=f"https://www.google.com/search?q={"weather in "+search}&oq={search}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8"


page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

temp = soup.find("div", class_="BNeawe").text

print(temp)