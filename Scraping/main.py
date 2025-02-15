# from selenium import webdriver
# driver = webdriver.Chrome()
# # driver.get("https://google.com")
# driver.get("https://google.com/search?q=wonderla+bangalore")
# # driver.get("https://google.com/search?q=wonderla+bangalore")

import requests

API_KEY = ""
PLACE_NAME = "Taj Mahal, India"
URL = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={PLACE_NAME}&inputtype=textquery&fields=place_id&key={API_KEY}"

response = requests.get(URL)
data = response.json()
print(data)

if data.get("candidates"):
    place_id = data["candidates"][0]["place_id"]
    print(f"Place ID: {place_id}")


d7ef08433e7a0b1b4cec488d3affb8d8eb1e2887409c90ae5d5cf0212e272888
