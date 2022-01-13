from bs4 import BeautifulSoup
import requests

location = input("Enter the city name:\n")
url = "https://google.com/search?q=temperature+in+" + location
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
temp = soup.find("div", class_="BNeawe").text
print(temp)